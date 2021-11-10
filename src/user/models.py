from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship

from src.core.base import Base


class User(Base):
    """Модель пользователя"""
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Post", back_populates="owner")
