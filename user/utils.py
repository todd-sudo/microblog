from typing import Optional

from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi import Request, Depends

from core.db import database
from user.models import users
from user.schemas import UserDB, UserCreate, User, UserUpdate

SECRET = "JH(&*TY(*&YUI(HJujhiughihi&T&*YT*(Y9978689YIJKLJLkjokljhbhiygh(*U"

# user_db = SQLAlchemyUserDatabase(UserDB, database, users)

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)


async def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, users)


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


fastapi_users = FastAPIUsers(
    get_user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
