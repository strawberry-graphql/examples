from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Post(BaseModel):
    """
    Represents a post in a Subreddit.
    """

    __tablename__ = "posts"

    title: str = Column(
        String(150),
        comment="""
        The title for the post.
        """,
    )

    text: Optional[str] = Column(
        String(1024),
        default=None,
        comment="""
        The text for the post.
        """,
    )

    link: Optional[str] = Column(
        String(255),
        default=None,
        unique=True,
        comment="""
        The link for the post.
        """,
    )

    thumbnail: Optional[str] = Column(
        String(255),
        default=None,
        comment="""
        The thumbnail URL for the post.
        """,
    )

    user_id: int = Column(
        Integer,
        ForeignKey("users.id"),
        comment="""
        The owner ID of the post.
        """,
    )

    subreddit_id: int = Column(
        Integer,
        ForeignKey("subreddits.id"),
        comment="""
        The SubReddit ID of the post.
        """,
    )

    votes: int = Column(
        Integer,
        default=1,
        comment="""
        The votes for the post.
        """,
    )

    comments = relationship("Comment", backref="post", lazy="dynamic")

    def __repr__(self) -> str:
        return "<Post %s>" % self.title
