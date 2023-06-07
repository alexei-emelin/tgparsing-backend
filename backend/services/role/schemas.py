import enum
from typing import Optional

from pydantic import BaseModel, Field


class RolesChoice(enum.Enum):
    user = "user"
    admin = "admin"
    accountant = "accountant"


class RoleGet(BaseModel):
    name: RolesChoice


class RolePatch(RoleGet):
    # Inherit name from RoreGet
    is_active: Optional[bool]
    permissions: Optional[dict]


class RoleResponse(RolePatch):
    # Inherit fields from RolePatch

    class Config:
        orm_mode = True


class Permissions(BaseModel):
    read: bool = False
    write: bool = False


class RoleCreate(BaseModel):
    name: str = Field(..., min_length=1, regex="^[a-zA-Z]+$")
    permissions: Permissions = Permissions()


class RoleUpdate(BaseModel):
    name: str = Field(..., min_length=1, regex="^[a-zA-Z]+$")
    permissions: Permissions = Permissions(read=True, write=False)