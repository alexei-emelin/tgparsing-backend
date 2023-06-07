from fastapi import APIRouter, Depends

from services.role import views
import services.role.schemas as role_schemas
from services.user.utils.permissions import is_superuser
from settings import config


router = APIRouter(prefix="/role", tags=["Role"])

router.add_api_route(
    path="/",
    endpoint=views.get_role,
    methods=["GET"],
    name=config.ROLE_GET,
    response_model=role_schemas.RoleResponse,
    dependencies=[Depends(is_superuser)],
)
router.add_api_route(
    path="/",
    endpoint=views.patch_role,
    methods=["PATCH"],
    name=config.ROLE_PATCH,
    response_model=role_schemas.RoleResponse,
    dependencies=[Depends(is_superuser)],
)
router.add_api_route(
    path="/all",
    endpoint=views.get_roles,
    methods=["GET"],
    name=config.ROLE_GET_ALL,
    dependencies=[Depends(is_superuser)],
)