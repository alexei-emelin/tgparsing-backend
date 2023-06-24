from typing import Optional, TypeVar

from fastapi import Form, UploadFile
from fastapi_users import schemas
from fastapi_users.schemas import CreateUpdateDictModel
from pydantic import BaseModel, EmailStr, Field
from services.role.schemas import RoleResponse


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class SuccessResponse(BaseModel):
    status: str


class UserRead(schemas.BaseUser):
    id: int
    firstname: str
    lastname: str
    email: EmailStr
    is_staff: bool
    avatar_url: str
    role: RoleResponse

    class Config:
        orm_mode = True


class UserCreate(CreateUpdateDictModel):
    firstname: str = Field(..., min_length=2, regex="^[a-zA-Zа-яА-яёЁ]+$")
    lastname: str = Field(..., min_length=2, regex="^[a-zA-Zа-яА-яёЁ]+$")
    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^\w\s]|.*[_]).",
    )


class UserPatch(CreateUpdateDictModel):
    firstname: Optional[str]
    lastname: Optional[str]
    password: Optional[str]
    avatar_url: Optional[UploadFile]

    @classmethod
    def as_form(
        cls,
        firstname: Optional[str] = Form(
            "", min_length=2, regex="^[a-zA-Zа-яА-яёЁ]+$"
        ),
        lastname: Optional[str] = Form(
            "", min_length=2, regex="^[a-zA-Zа-яА-яёЁ]+$"
        ),
        password: Optional[str] = Form(
            "",
            min_length=8,
            regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^\w\s]|.*[_]).",
        ),
        avatar_url: Optional[UploadFile] = Form(None, alias="picture"),
    ):
        return cls(
            firstname=firstname,
            lastname=lastname,
            password=password,
            avatar_url=avatar_url,
        )


class UserUpdate(schemas.BaseUserUpdate):
    pass


UP = TypeVar("UP", bound=UserPatch)
