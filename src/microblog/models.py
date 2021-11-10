from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.core.base_class import Base


class Post(Base):
    """ Модель Поста
    """
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(length=320))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")
