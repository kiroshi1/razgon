from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.core.auth import auth_backend, fastapi_users
from app.core.config import settings
from app.core.database import SessionLocal
from app.schemas.user import UserCreate, UserRead, UserUpdate


def get_db():
    """Получить сессию базы данных."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title=settings.PROJECT_NAME)

# Подключение роутов аутентификации
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/")
def root():
    """Корневой endpoint."""
    return {"message": f"Добро пожаловать в {settings.PROJECT_NAME}!"}


@app.get("/hello")
def hello_world(db: Annotated[Session, Depends(get_db)]):
    """Тестовый endpoint."""
    return {"message": f"Hello from {settings.PROJECT_NAME}!"}
