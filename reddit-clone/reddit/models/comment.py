from typing import Optional

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Comment(BaseModel):
    """
    Represents a Comment in a thread.
    """

    content: str = Column(
        Text,
        nullable=False,
        comment="""
        The content of the comment.
        """,
    )

    votes: int = Column(
        Integer,
        default=1,
        comment="""
        The votes for the thread.
        """,
    )

    user_id: Optional[int] = Column(
        Integer,
        ForeignKey("users.id"),
        comment="""
        The owner ID of the comment.
        """,
    )

    replies = relationship("Comment", backref="parent", lazy="dynamic")

    def __repr__(self) -> str:
        return "<Comment %s>" % self.id
