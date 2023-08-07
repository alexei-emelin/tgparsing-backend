import aiofiles
import fastapi as fa
from services.role.schemas import RoleNameChoice
from services.user import db_handlers as db_hand
from services.user import schemas as user_schema
from services.user.models import User
from services.user.utils import security
from settings import config
from sqlalchemy.ext.asyncio import AsyncSession


async def update_user(
    session: AsyncSession,
    changing_user: User,
    current_user: User,
    update_data: user_schema.UserPatch | user_schema.UserPatchByAdmin,
) -> User | None:
    data = update_data.dict()
    if not data:
        raise fa.HTTPException(
            status_code=fa.status.HTTP_400_BAD_REQUEST,
            detail="Нет данных для изменений",
        )
    if data.get("avatar_url"):
        folder_path = config.static_dir_url / config.AVATARS_FOLDER
        file_name = (
            f"{changing_user.email}"
            f".{data['avatar_url'].filename.split('.')[-1]}"
        )
        file_url = folder_path / file_name
        async with aiofiles.open(file_url, "wb") as p_f:
            await p_f.write(data["avatar_url"].file.read())
        data["avatar_url"] = str(file_url)
    if data.get("hashed_password"):
        data["hashed_password"] = security.get_hash_password(
            data["hashed_password"]
        )
    if (
        data.get("role_name")
        and current_user.role_name is not RoleNameChoice.SUPERUSER
    ):
        raise fa.HTTPException(
            status_code=fa.status.HTTP_403_FORBIDDEN,
            detail="Изменение роли недоступно",
        )
    user_db = await db_hand.update_user(session, changing_user.id, data)
    return user_db
