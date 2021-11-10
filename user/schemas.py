from fastapi_users import models


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    name: str


class UserUpdate(models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
