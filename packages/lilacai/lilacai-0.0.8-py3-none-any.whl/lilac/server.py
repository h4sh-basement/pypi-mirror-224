"""Serves the Lilac server."""

import asyncio
import logging
import os
import shutil
import webbrowser
from typing import Any, Optional

import uvicorn
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, ORJSONResponse
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from . import (
  router_concept,
  router_data_loader,
  router_dataset,
  router_google_login,
  router_signal,
  router_tasks,
)
from .auth import (
  AuthenticationInfo,
  ConceptAuthorizationException,
  UserInfo,
  get_session_user,
  get_user_access,
)
from .concepts.db_concept import CONCEPTS_DIR, DiskConceptDB, get_concept_output_dir
from .db_manager import list_datasets
from .env import data_path, env
from .router_utils import RouteErrorHandler
from .tasks import task_manager
from .utils import get_dataset_output_dir, get_lilac_cache_dir

DIST_PATH = os.path.join(os.path.dirname(__file__), 'web')

tags_metadata: list[dict[str, Any]] = [{
  'name': 'datasets',
  'description': 'API for querying a dataset.',
}, {
  'name': 'concepts',
  'description': 'API for managing concepts.',
}, {
  'name': 'data_loaders',
  'description': 'API for loading data.',
}, {
  'name': 'signals',
  'description': 'API for managing signals.',
}]


def custom_generate_unique_id(route: APIRoute) -> str:
  """Generate the name for the API endpoint."""
  return route.name


app = FastAPI(
  default_response_class=ORJSONResponse,
  generate_unique_id_function=custom_generate_unique_id,
  openapi_tags=tags_metadata)


@app.exception_handler(ConceptAuthorizationException)
def concept_authorization_exception(request: Request,
                                    exc: ConceptAuthorizationException) -> JSONResponse:
  """Return a 401 JSON response when an authorization exception is thrown."""
  return JSONResponse(
    status_code=401,
    content={'message"': 'Oops! You are not authorized to do this.'},
  )


app.add_middleware(SessionMiddleware, secret_key=env('LILAC_OAUTH_SECRET_KEY'))

app.include_router(router_google_login.router, prefix='/google', tags=['google_login'])

v1_router = APIRouter(route_class=RouteErrorHandler)
v1_router.include_router(router_dataset.router, prefix='/datasets', tags=['datasets'])
v1_router.include_router(router_concept.router, prefix='/concepts', tags=['concepts'])
v1_router.include_router(router_data_loader.router, prefix='/data_loaders', tags=['data_loaders'])
v1_router.include_router(router_signal.router, prefix='/signals', tags=['signals'])
v1_router.include_router(router_tasks.router, prefix='/tasks', tags=['tasks'])


@app.get('/auth_info')
def auth_info(request: Request) -> AuthenticationInfo:
  """Returns the user's ACL.

  NOTE: Validation happens server-side as well. This is just used for UI treatment.
  """
  user_info: Optional[UserInfo] = get_session_user(request)
  return AuthenticationInfo(
    user=user_info, access=get_user_access(), auth_enabled=env('LILAC_AUTH_ENABLED', False))


app.include_router(v1_router, prefix='/api/v1')

current_dir = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(current_dir, 'templates'))


@app.get('/_data{path:path}', response_class=HTMLResponse, include_in_schema=False)
def list_files(request: Request, path: str) -> Response:
  """List files in the data directory."""
  if env('LILAC_AUTH_ENABLED', False):
    return Response(status_code=401)
  path = os.path.join(data_path(), f'.{path}')
  if not os.path.exists(path):
    return Response(status_code=404)
  if os.path.isfile(path):
    return FileResponse(path)

  files = os.listdir(path)
  files_paths = sorted([(os.path.join(request.url.path, f), f) for f in files])
  return templates.TemplateResponse('list_files.html', {'request': request, 'files': files_paths})


@app.api_route('/{path_name}', include_in_schema=False)
def catch_all() -> FileResponse:
  """Catch any other requests and serve index for HTML5 history."""
  return FileResponse(path=os.path.join(DIST_PATH, 'index.html'))


# Serve static files in production mode.
app.mount('/', StaticFiles(directory=DIST_PATH, html=True, check_dir=False))


@app.on_event('startup')
def startup() -> None:
  """Download dataset files from the HF space that was uploaded before building the image."""
  # SPACE_ID is the HuggingFace Space ID environment variable that is automatically set by HF.
  repo_id = env('SPACE_ID', None)

  if repo_id:
    # Copy datasets.
    spaces_data_dir = 'data'
    datasets = list_datasets(spaces_data_dir)
    for dataset in datasets:
      spaces_dataset_output_dir = get_dataset_output_dir(spaces_data_dir, dataset.namespace,
                                                         dataset.dataset_name)
      persistent_output_dir = get_dataset_output_dir(data_path(), dataset.namespace,
                                                     dataset.dataset_name)
      shutil.rmtree(persistent_output_dir, ignore_errors=True)
      shutil.copytree(spaces_dataset_output_dir, persistent_output_dir, dirs_exist_ok=True)
      shutil.rmtree(spaces_dataset_output_dir, ignore_errors=True)

    # Delete cache files from persistent storage.
    cache_dir = get_lilac_cache_dir(data_path())
    if os.path.exists(cache_dir):
      shutil.rmtree(cache_dir)

    # NOTE: This is temporary during the move of concepts into the pip package. Once all the demos
    # have been updated, this block can be deleted.
    old_lilac_concepts_data_dir = os.path.join(data_path(), CONCEPTS_DIR, 'lilac')
    if os.path.exists(old_lilac_concepts_data_dir):
      shutil.rmtree(old_lilac_concepts_data_dir)

    # Copy cache files from the space if they exist.
    spaces_cache_dir = get_lilac_cache_dir(spaces_data_dir)
    if os.path.exists(spaces_cache_dir):
      shutil.copytree(spaces_cache_dir, cache_dir)

    # Copy concepts.
    concepts = DiskConceptDB(spaces_data_dir).list()
    for concept in concepts:
      # Ignore lilac concepts, they're already part of the source code.
      if concept.namespace == 'lilac':
        continue
      spaces_concept_output_dir = get_concept_output_dir(spaces_data_dir, concept.namespace,
                                                         concept.name)
      persistent_output_dir = get_concept_output_dir(data_path(), concept.namespace, concept.name)
      shutil.rmtree(persistent_output_dir, ignore_errors=True)
      shutil.copytree(spaces_concept_output_dir, persistent_output_dir, dirs_exist_ok=True)
      shutil.rmtree(spaces_concept_output_dir, ignore_errors=True)


@app.on_event('shutdown')
async def shutdown_event() -> None:
  """Kill the task manager when FastAPI shuts down."""
  await task_manager().stop()


class GetTasksFilter(logging.Filter):
  """Task filter for /tasks."""

  def filter(self, record: logging.LogRecord) -> bool:
    """Filters out /api/v1/tasks/ from the logs."""
    return record.getMessage().find('/api/v1/tasks/') == -1


logging.getLogger('uvicorn.access').addFilter(GetTasksFilter())

SERVER: Optional[uvicorn.Server] = None


def start_server(host: str = '0.0.0.0', port: int = 5432, open: bool = False) -> None:
  """Starts the Lilac web server.

  Args:
    host: The host to run the server on.
    port: The port to run the server on.
    open: Whether to open a browser tab upon startup.
  """
  global SERVER
  if SERVER:
    raise ValueError('Server is already running')

  config = uvicorn.Config(
    app,
    host=host,
    port=port,
    access_log=False,
  )
  SERVER = uvicorn.Server(config)

  if open:

    @app.on_event('startup')
    def open_browser() -> None:
      webbrowser.open(f'http://{host}:{port}')

  try:
    loop = asyncio.get_event_loop()
    if loop.is_running():
      loop.create_task(SERVER.serve())
    else:
      SERVER.run()
  except RuntimeError:
    SERVER.run()


async def stop_server() -> None:
  """Stops the Lilac web server."""
  global SERVER
  if SERVER is None:
    raise ValueError('Server is not running')
  await SERVER.shutdown()
  SERVER = None
