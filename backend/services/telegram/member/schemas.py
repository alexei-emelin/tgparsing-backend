from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class GetAllMembers(BaseModel):
    chat_id: Optional[str]


class Parser(BaseModel):
    api_id: int
    api_hash: str
    session_string: str


class ParserBySubscribes(Parser):
    chats: List[str]


class ParserByPeriod(ParserBySubscribes):
    period_from: date
    period_to: date


class ParserPrivateChanels(ParserBySubscribes):
    limit: int


class ParserByGeo(Parser):
    lat: float
    lng: float
    accuracy_radius: int = 500


class ChatMember(BaseModel):
    user_id: int
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    username: str


class ChatMemberRead(ChatMember):
    id: int

    class Config:
        orm_mode = True


class ParsedChat(BaseModel):
    chat_id: int
    username: str
    description: Optional[str] = None
    title: Optional[str] = None


class ParsedChatRead(ParsedChat):
    id: int

    class Config:
        orm_mode = True
