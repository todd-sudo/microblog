from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.microblog.models import Post
from src.microblog.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: PostCreate, user_id: int
    ) -> Post:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Post]:
        return (
            db.query(self.model)
            .filter(Post.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


crud_post = CRUDPost(Post)
