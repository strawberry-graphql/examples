from typing import Optional
from datetime import datetime

from sqlalchemy import Column

from reddit.db.base import Base


class BaseModel(Base):
    """
    The base class which every model
    must subclass/ inherit from.
    """

    __abstract__ = True

    id: Optional[int] = Column(
        default=None,
        primary_key=True,
        comment="""
        Identifier for the object.
        """,
    )

    created_at: datetime = Column(
        nullable=False,
        default=datetime.now(),
        comment="""
        When the object was created.
        """,
    )

    updated_at: datetime = Column(
        nullable=False,
        default=datetime.now(),
        onupdate=datetime.now(),
        comment="""
        When the object was updated.
        """,
    )
