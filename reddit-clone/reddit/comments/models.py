from __future__ import annotations

from typing import Optional, List

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Comment(Base):
    """
    Represents a Comment on a post.
    """

    __tablename__ = "comments"

    id: int = Column(Integer, primary_key=True, nullable=False)

    content: str = Column(Text, nullable=False)

    votes: int = Column(Integer, default=1)

    user_id: Optional[int] = Column(Integer, ForeignKey("users.id"))

    post_id: int = Column(Integer, ForeignKey("posts.id"))

    replies: List[Comment] = relationship(
        "Comment", back_populates="parent", lazy="dynamic"
    )

    def __repr__(self) -> str:
        return f"<Comment {self.id}>"
