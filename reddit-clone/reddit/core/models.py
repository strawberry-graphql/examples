from typing import Optional
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
    """
    The base class which every model
    must subclass/ inherit from.
    """

    __abstract__ = True

    id: Optional[int] = Column(
        default=None,
        primary_key=True,
        description="""
        Identifier for the object.
        """,
    )

    created_at: datetime = Column(
        nullable=False,
        default=datetime.now(),
        description="""
        When the object was created.
        """,
    )

    updated_at: datetime = Column(
        nullable=False,
        default=datetime.now(),
        onupdate=datetime.now(),
        description="""
        When the object was updated.
        """,
    )
