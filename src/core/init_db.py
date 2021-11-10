from sqlalchemy.orm import Session

from src.user.services import user
from src.user.schemas import user as user_schemas
from src.config.settings import settings
from src.core.db import Base


def init_db(db: Session) -> None:
    _user = user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not _user:
        user_in = user_schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        _user = user.create(db, obj_in=user_in)
