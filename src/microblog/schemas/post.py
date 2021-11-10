from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    id: int
    title: str
    text: Optional[str] = None
    date: datetime

    class Config:
        orm_mode = True


class PostList(PostBase):
    pass


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostInDB(PostBase):
    pass
