from datetime import date, datetime
from typing import List

from pydantic import BaseModel, Field, validator


class GetChats(BaseModel):
    task_name: str
    query: str = Field(description="Ключевое слово")


class GetMembers(BaseModel):
    task_name: str
    parsed_chats: List[str] = Field(
        min_items=1,
        max_items=5,
        unique_items=True,
        description="Чаты для парсинга",
    )
    groups_count: int = Field(default=1)

    @validator("parsed_chats", pre=True)
    def check_chats(cls, value):  # pylint: disable=E0213
        new_value = []
        for item in value:
            new_value.append(item.split("/")[-1])
        return new_value

    @validator("groups_count")
    def check_groups_count(cls, value, values):  # pylint: disable=E0213
        if value > len(values["parsed_chats"]):
            raise ValueError(
                "Количество групп не должно превышать "
                "количество переданных чатов."
            )
        return value


class GetActiveMembers(BaseModel):
    task_name: str
    parsed_chats: List[str] = Field(
        min_items=1,
        max_items=5,
        unique_items=True,
        description="Чаты для парсинга",
    )
    from_date: date
    to_date: date

    @validator("from_date")
    def change_from_date(cls, value):  # pylint: disable=E0213
        return str(datetime.combine(value, datetime.min.time()))

    @validator("to_date")
    def change_to_date(cls, value):  # pylint: disable=E0213
        return str(
            datetime.combine(value, datetime.max.time().replace(microsecond=0))
        )


class GetByGeo(BaseModel):
    task_name: str
    latitude: float
    longitude: float
    accuracy_radius: int = Field(description="In meters")