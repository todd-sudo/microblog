from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.microblog.service import crud_post
from src.service import get_db
from src.microblog import schemas
from src.user.models import User
from src.user.utils import get_current_active_user
from src.user.services import crud_user


router = APIRouter()


@router.get("/", response_model=List[schemas.Post])
def read_posts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Retrieve posts.
    """
    if crud_user.is_superuser(current_user):
        posts = crud_post.get_multi(db, skip=skip, limit=limit)
    else:
        posts = crud_post.get_multi_by_owner(
            db=db, user_id=current_user.id, skip=skip, limit=limit
        )
    return posts


@router.post("/", response_model=schemas.Post)
def create_post(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.PostCreate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """ Create new post.
    """
    print(current_user.email)
    post = crud_post.create_with_owner(
        db=db, obj_in=item_in, user_id=current_user.id
    )
    return post


@router.put("/{id}", response_model=schemas.Post)
def update_post(
    *,
    db: Session = Depends(get_db),
    id: int,
    post_in: schemas.PostUpdate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """ Update an post.
    """
    post = crud_post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud_user.is_superuser(current_user) and (post.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    post = crud_post.update(db=db, db_obj=post, obj_in=post_in)
    return post


@router.get("/{id}", response_model=schemas.Post)
def read_post(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """ Get post by ID.
    """
    post = crud_post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud_user.is_superuser(current_user) and (post.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return post


@router.delete("/{id}", response_model=schemas.Post)
def delete_post(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """ Delete an post.
    """
    post = crud_post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if not crud_user.is_superuser(current_user) and (post.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    post = crud_post.remove(db=db, id=id)
    return post
