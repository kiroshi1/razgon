import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    """Схема для чтения пользователя."""

    first_name: str | None
    last_name: str | None


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания пользователя."""

    first_name: str | None = None
    last_name: str | None = None


class UserUpdate(schemas.BaseUserUpdate):
    """Схема для обновления пользователя."""

    first_name: str | None = None
    last_name: str | None = None
