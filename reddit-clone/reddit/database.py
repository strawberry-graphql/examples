from contextlib import asynccontextmanager
from typing import Generator

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base


from reddit.core.config import DATABASE_URI

async_engine = create_async_engine(DATABASE_URI, future=True)

session_factory = sessionmaker(bind=async_engine, class_=AsyncSession)


@asynccontextmanager
async def get_session() -> Generator[AsyncSession]:
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
