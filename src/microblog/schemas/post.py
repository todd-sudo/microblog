from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None


class PostCreate(PostBase):
    title: str


class PostUpdate(PostBase):
    pass


class PostInDBBase(PostBase):
    id: int
    title: str
    date: datetime = datetime.now()
    user_id: int

    class Config:
        orm_mode = True


class Post(PostInDBBase):
    pass


class PostInDB(PostInDBBase):
    pass
