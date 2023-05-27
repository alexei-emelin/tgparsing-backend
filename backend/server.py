from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from database.models.user_model import User


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app = FastAPI(title='TgParsing')

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


# current_user = fastapi_users.current_user()
#
#
# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.firstname}"
