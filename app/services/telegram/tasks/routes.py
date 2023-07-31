from typing import List

import fastapi as fa
from services.telegram.tasks import schemas, views
from services.user.utils import permissions as perm
from settings import config


task_router = fa.APIRouter(prefix="/tasks", tags=["Tasks"])

task_router.add_api_route(
    path="/",
    endpoint=views.get_tasks,
    methods=["GET"],
    name=config.TASK_GET_ALL,
    response_model=List[schemas.GetTasksResponse],
    dependencies=[fa.Depends(perm.is_admin)],
    description="Get all tasks. This endpoint can use admin or superuser",
)
task_router.add_api_route(
    path="/me",
    endpoint=views.get_user_tasks,
    methods=["GET"],
    name=config.TASK_ME_GET_ALL,
    response_model=List[schemas.GetTasksResponse],
    dependencies=[fa.Depends(perm.is_user)],
    description="Get all user tasks. This endpoint can use user",
)
task_router.add_api_route(
    path="/me",
    endpoint=views.delete_task,
    methods=["DELETE"],
    name=config.TASK_ME_DELETE,
    dependencies=[fa.Depends(perm.is_user)],
    description="Delete current user task. This endpoint can use user",
)
task_router.add_api_route(
    path="/me/download",
    endpoint=views.download_file,
    methods=["GET"],
    name=config.TASK_ME_DOWNLOAD_FILE,
    dependencies=[fa.Depends(perm.is_user)],
    description="Download file from user task that has status 'success'. "
    "This endpoint can use user",
)
