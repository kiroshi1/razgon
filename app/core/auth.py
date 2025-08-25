import uuid

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from app.core.config import settings
from app.core.users import get_user_manager
from app.models.user import User

# Настройка транспорта токенов
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


# Настройка JWT стратегии
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_KEY, lifetime_seconds=3600)


# Создание бэкенда аутентификации
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# Основной объект FastAPI Users
fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

# Функции для получения текущего пользователя
current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
