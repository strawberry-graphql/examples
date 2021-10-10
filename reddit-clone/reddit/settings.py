from typing import Optional

from starlette.config import Config


config = Config(env_file=".env")

# whether the application is in development mode.
DEBUG: bool = config("DEBUG", cast=bool, default=False)

# SQLAlchemy database URL.
DATABASE_URI: str = config("DATABASE_URI", cast=str)

# mail client configuration.
MAIL_HOST: str = config("MAIL_HOST", cast=str)
MAIL_PORT: int = config("MAIL_PORT", cast=int)
MAIL_USERNAME: Optional[str] = config("MAIL_USERNAME", cast=str, default=None)
MAIL_PASSWORD: Optional[str] = config("MAIL_PASSWORD", cast=str, default=None)
MAIL_SENDER: Optional[str] = config("MAIL_SENDER", cast=str, default=None)
