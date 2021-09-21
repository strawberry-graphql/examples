from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from reddit.core.models import BaseModel


class Thread(BaseModel):
    """
    Represents a Thread in a SubReddit.
    """

    __tablename__ = "threads"

    title: str = Column(
        String(150),
        comment="""
        The title for the thread.
        """,
    )

    text: Optional[str] = Column(
        String(1024),
        default=None,
        comment="""
        The text for the thread.
        """,
    )

    link: Optional[str] = Column(
        String(255),
        default=None,
        comment="""
        The link for the thread.
        """,
    )

    thumbnail: Optional[str] = Column(
        String(255),
        default=None,
        comment="""
        The thumbnail URL for the thread.
        """,
    )

    user_id: int = Column(
        Integer,
        ForeignKey("users.id"),
        comment="""
        The owner ID the thread.
        """,
    )

    subreddit_id: int = Column(
        Integer,
        ForeignKey("subreddits.id"),
        comment="""
        The SubReddit ID of the thread.
        """,
    )

    votes: int = Column(
        Integer,
        default=1,
        comment="""
        The votes for the thread.
        """,
    )

    comments = relationship("Comment", backref="thread", lazy="dynamic")

    def __repr__(self) -> str:
        return "<Thread %s>" % self.title
