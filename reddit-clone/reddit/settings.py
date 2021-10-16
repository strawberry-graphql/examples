from typing import Optional

from starlette.config import Config


config = Config(env_file=".env")

# whether the application is in development mode.
DEBUG: bool = config("DEBUG", cast=bool, default=False)

# SQLAlchemy database URL.
DATABASE_URL: str = config("DATABASE_URL", cast=str)

# mail client host name.
MAIL_HOST: str = config("MAIL_HOST", cast=str)

# mail client port.
MAIL_PORT: int = config("MAIL_PORT", cast=int)

# mail client auth username.
MAIL_USERNAME: Optional[str] = config("MAIL_USERNAME", cast=str, default=None)

# mail client auth password.
MAIL_PASSWORD: Optional[str] = config("MAIL_PASSWORD", cast=str, default=None)

# mail client sender address.
MAIL_SENDER: Optional[str] = config("MAIL_SENDER", cast=str, default=None)

# celery broker URL.
CELERY_BROKER: str = config("CELERY_BROKER", cast=str)

# celery result backend URL.
CELERY_BACKEND: str = config("CELERY_BACKEND", cast=str)
