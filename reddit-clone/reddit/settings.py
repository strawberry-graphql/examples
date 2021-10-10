from starlette.config import Config


config = Config(env_file=".env")

# whether the application is in development mode.
DEBUG: bool = config("DEBUG", cast=bool, default=False)

# sqlalchemy database url.
DATABASE_URI: str = config("DATABASE_URI", cast=str)

# mail configuration.
MAIL_HOST: str = config("MAIL_HOST", cast=str)
MAIL_PORT: int = config("MAIL_PORT", cast=int)
MAIL_USERNAME: str = config("MAIL_USERNAME", cast=str)
MAIL_PASSWORD: str = config("MAIL_PASSWORD", cast=str)
MAIL_SENDER: str = config("MAIL_SENDER", cast=str)
