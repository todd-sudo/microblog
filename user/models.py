from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Integer, DateTime, Boolean

from core.db import Base


class User(Base, SQLAlchemyBaseUserTable):
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(length=100), unique=True)
    date = Column(DateTime)


users = User.__table__


# from sqlalchemy import Column, String, Integer, DateTime, Boolean
#
# from core.db import Base
#
#
# class User(Base):
#     """ Модель Пользователя
#     """
#     __tablename__ = "user"
#
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     name = Column(String(length=100), unique=True)
#     email = Column(String(length=200), unique=True)
#     password = Column(String)
#     date = Column(DateTime)
#     is_active = Column(Boolean, default=False)
#     is_admin = Column(Boolean, default=False)
