from fastapi import FastAPI

from routes import routes


app = FastAPI()


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal sever error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response


app.include_router(routes)


