from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from reddit import settings

engine = create_async_engine(settings.DATABASE_URI, future=True)

session_factory = sessionmaker(bind=engine, class_=AsyncSession)

__all__ = ("get_session", "Base")


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Gets a session instance.

    :return: the obtained session.
    """
    session = session_factory()
    try:
        yield session
        await session.commit()
    except Exception as err:
        await session.rollback()
        raise err
    finally:
        await session.close()


Base = declarative_base()
