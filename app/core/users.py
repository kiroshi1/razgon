import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.db import SQLAlchemyUserDatabase

from app.core.config import settings
from app.models.user import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """Менеджер пользователей."""

    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """Действие после регистрации пользователя."""
        print(f"Пользователь {user.id} зарегистрирован.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        """Действие после запроса сброса пароля."""
        print(f"Пользователь {user.id} запросил сброс пароля. Токен: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        """Действие после запроса верификации."""
        print(f"Пользователь {user.id} запросил верификацию. Токен: {token}")


async def get_user_db():
    """Получить экземпляр базы данных пользователей."""
    from app.core.database import async_session_maker

    async with async_session_maker() as session:
        yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    """Получить менеджер пользователей."""
    yield UserManager(user_db)
