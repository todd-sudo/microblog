import secrets
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, PostgresDsn


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM = "HS256"
    SERVER_NAME: str = "localhost"
    # SERVER_HOST: AnyHttpUrl = "postgresql"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str = "FastBlog"

    POSTGRES_SERVER: str = "postgresql"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "qwerty"
    POSTGRES_DB: str = "microblog"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = "postgresql://postgres:qwerty@localhost:5436/microblog"

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = 587
    SMTP_HOST: Optional[str] = "smtp.gmail.com"
    SMTP_USER: Optional[str] = "mrrobot20332034@gmail.com"
    SMTP_PASSWORD: Optional[str] = "icygvnblerifelso"
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48

    EMAIL_TEMPLATES_DIR: str = "/src/email-templates/build"
    EMAILS_ENABLED: bool = False

    EMAIL_TEST_USER: EmailStr = "todd.develop@gmail.com"
    FIRST_SUPERUSER: EmailStr = "todd.develop@gmail.com"
    FIRST_SUPERUSER_PASSWORD: str = "123456"
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True


settings = Settings()
