import enum
from typing import Optional

from pydantic import BaseModel, Field


class WorkChoice(enum.Enum):
    WORK = "work"
    FREE = "free"


class BlockChoice(enum.Enum):
    BLOCK = "block"
    UNBLOCK = "unblock"


class TgAccountBase(BaseModel):
    api_id: int
    api_hash: str
    # session_string: str

    class Config:
        orm_mode = True


class TgAccountRead(TgAccountBase):
    # Inherit api_id, api_hash and session_string from parent
    id: int
    work_status: WorkChoice = WorkChoice.FREE
    block_status: BlockChoice = BlockChoice.UNBLOCK


class TgAccountCreate(TgAccountBase):
    # Inherit api_id, api_hash and session_string from parent
    phone_number: str = Field(
        default=...,
    )  # regex="^\+7\d{10}$")


class TgAccountUpdate(BaseModel):
    api_id: Optional[int] = Field(default=None)
    api_hash: Optional[str] = Field(default=None)
    session_string: Optional[str] = Field(default=None)
    work_status: Optional[WorkChoice] = Field(default=None)
    block_status: Optional[BlockChoice] = Field(default=None)


class TgAccountGetAll(BaseModel):
    work_status: Optional[WorkChoice] = Field(default=None)
    block_status: Optional[BlockChoice] = Field(default=None)
