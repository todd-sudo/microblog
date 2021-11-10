from fastapi import APIRouter

from microblog import api
from user import routes as user_routes


routes = APIRouter()

routes.include_router(api.router, prefix="/blog")
routes.include_router(user_routes.router)
