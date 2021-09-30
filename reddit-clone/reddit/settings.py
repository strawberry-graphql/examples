from starlette.config import Config


config = Config(env_file=".env")

# whether the application is in development mode.
DEBUG: bool = config("DEBUG", cast=bool, default=False)

# sqlalchemy database url.
DATABASE_URI: str = config("DATABASE_URI", cast=str)
