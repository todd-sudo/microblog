from fastapi import FastAPI

from routes import routes
from src.config.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME, 
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal sever error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response


app.include_router(routes, prefix=settings.API_V1_STR)


