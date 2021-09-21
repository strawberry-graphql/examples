from starlette.config import Config
from starlette.datastructures import Secret


config = Config(env_file=".env")

# whether the application is in development mode.
DEBUG: bool = config("DEBUG", cast=bool, default=False)

# secret key to use for sessions.
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)
