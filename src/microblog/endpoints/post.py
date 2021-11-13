from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.microblog.service import crud_post
from src.service import get_db
from src.microblog import schemas
from src.user.models import User
from src.user.utils import get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[schemas.PostList])
def read_posts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Retrieve items.
    """
    if crud_post.is_superuser(current_user):
        items = crud_post.get_multi(db, skip=skip, limit=limit)
    else:
        items = crud_post.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return items


@router.post("/", response_model=schemas.PostCreate)
def create_item(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.PostCreate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    item = crud_post.create_with_owner(
        db=db, obj_in=item_in, owner_id=current_user.id
    )
    return item


@router.put("/{id}", response_model=schemas.PostUpdate)
def update_post(
    *,
    db: Session = Depends(get_db),
    id: int,
    item_in: schemas.PostUpdate,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """ Update an item.
    """
    post = crud_post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud_post.is_superuser(current_user) and (post.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    post = crud_post.update(db=db, db_obj=post, obj_in=item_in)
    return post


@router.get("/{id}", response_model=schemas.PostDetail)
def read_post(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """ Get item by ID.
    """
    post = crud_post.item.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud_post.user.is_superuser(current_user) and (post.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return post


@router.delete("/{id}", response_model=schemas.PostDetail)
def delete_post(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """ Delete an item.
    """
    item = crud_post.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not crud_post.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud_post.item.remove(db=db, id=id)
    return item
