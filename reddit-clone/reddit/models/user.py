from typing import Optional

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class User(BaseModel):
    """
    Represents an individual user account.
    """

    __tablename__ = "users"

    username: str = Column(
        String(32),
        nullable=False,
        unique=True,
        comment="""
        The username for the user.
        """,
    )

    email: str = Column(
        String(255),
        nullable=False,
        unique=True,
        comment="""
        The email for the user.
        """,
    )

    password: str = Column(
        String(255),
        nullable=False,
        comment="""
        The password for the user.
        """,
    )

    avatar: Optional[str] = Column(
        String(255),
        default=None,
        comment="""
        The avatar URL for the user.
        """,
    )

    posrs = relationship("Post", backref="user", lazy="dynamic")

    subreddits = relationship("Subreddit", backref="user", lazy="dynamic")

    comments = relationship("Comment", backref="user", lazy="dynamic")

    def __repr__(self) -> str:
        return "<User %s>" % self.username
