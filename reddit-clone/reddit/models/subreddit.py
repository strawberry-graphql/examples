from typing import Optional

from sqlalchemy import Column, String, Integer, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Subreddit(BaseModel):
    """
    Represents a Subreddit.
    """

    __tablename__ = "subreddits"

    name: str = Column(
        String(75),
        unique=True,
        nullable=False,
        comment="""
        The name for the subreddit.
        """,
    )

    description: Optional[str] = Column(
        String(255),
        default=None,
        comment="""
        The description for the subreddit.
        """,
    )

    admin_id: int = Column(
        Integer,
        ForeignKey("users.id"),
        comment="""
        The admin ID of the subreddit.
        """,
    )

    status: int = Column(
        SmallInteger,
        comment="""
        The status of the subreddit.
        """,
    )

    icon: Optional[str] = Column(
        String(255),
        default=None,
        comment="""
        The icon URL for the subreddit.
        """,
    )

    posts = relationship("Post", backref="subreddit", lazy="dynamic")

    def __repr__(self) -> str:
        return "<SubReddit %s>" % self.name