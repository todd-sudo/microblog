from fastapi import APIRouter

from src.user.endpoints import login, users
from src.microblog.endpoints import post


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(post.router, prefix="/posts", tags=["posts"])
