import decimal
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from fastapi import Form, UploadFile
from pydantic import BaseModel, EmailStr, Field
from services.role.schemas import RoleNameChoice, RoleResponse
from services.tariff.schemas import UserSubscribeResponse


NAME_PATTER = (
    "^(([а-яА-ЯёЁ][а-яё]*)(-[а-яА-ЯёЁ][а-яё]*)?)|"
    "(([a-zA-Z][a-z]*)(-[a-zA-Z][a-z]*)?)$"
)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class SuccessResponse(BaseModel):
    status: str


class UserRead(BaseModel):
    id: int
    firstname: str | None
    lastname: str | None
    email: EmailStr
    timezone: int
    is_staff: bool
    is_active: bool = True
    is_verified: bool = False
    avatar_url: str
    role: RoleResponse
    phone_number: str | None
    created_at: datetime
    balance: decimal.Decimal
    subscribe: UserSubscribeResponse | None

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    hashed_password: str = Field(
        ...,
        alias="password",
        min_length=8,
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^\w\s]|.*[_]).",
    )
    timezone: Optional[int] = Field(default=0, ge=-12, le=12)


@dataclass
class UserPatch:
    firstname: Optional[str] = Form(
        default=None,
        min_length=1,
        max_length=61,
        regex=NAME_PATTER,
    )
    lastname: Optional[str] = Form(
        default=None,
        min_length=1,
        max_length=61,
        regex=NAME_PATTER,
    )
    timezone: Optional[int] = Form(default=None, ge=-12, le=12)
    hashed_password: Optional[str] = Form(
        default=None,
        min_length=8,
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^\w\s]|.*[_]).",
        alias="password",
    )
    avatar_url: Optional[UploadFile] = Form(default=None, alias="picture")
    email: Optional[EmailStr] = Form(default=None)
    phone_number: Optional[str] = Form(
        default=None,
        min_length=8,
        regex=r"^\+[0-9+][0-9()-]{4,14}\d$",
    )


@dataclass
class UserPatchByAdmin(UserPatch):
    is_staff: Optional[bool] = Form(default=None)
    role_name: Optional[RoleNameChoice] = Form(default=None, alias="role")
    is_active: Optional[bool] = Form(default=None)


class UserPatchResponse(BaseModel):
    firstname: str | None
    lastname: str | None
    email: EmailStr
    hashed_password: str
    timezone: int
    avatar_url: str
    phone_number: str | None

    class Config:
        orm_mode = True


class UserPatchByAbminResponse(UserPatchResponse):
    is_staff: bool
    is_active: bool = True
    is_verified: bool = False
    role_name: RoleNameChoice
