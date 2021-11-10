from fastapi import APIRouter

from src.api import api_router


routes = APIRouter()

routes.include_router(api_router)
