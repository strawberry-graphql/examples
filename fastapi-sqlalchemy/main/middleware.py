from starlette.authentication import AuthenticationBackend, BaseUser, AuthCredentials

from main.auth import get_user
from main.database import SessionLocal
from main.models import User


class ProxyDBUser(BaseUser):
    def __init__(self, instance: User):
        self.instance = instance

    # Proxy attributes from instance
    def __getattr__(self, name):
        return getattr(self.instance, name)

    @property
    def is_authenticated(self) -> bool:
        return True


class SessionBackend(AuthenticationBackend):
    async def authenticate(self, request):
        db = SessionLocal()
        user = get_user(db, request)

        if not user:
            return

        return AuthCredentials(["authenticated"]), ProxyDBUser(user)
