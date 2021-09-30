from typing import Optional

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Comment(Base):
    """
    Represents a Comment in a thread.
    """

    content: str = Column(Text, nullable=False)

    votes: int = Column(Integer, default=1)

    user_id: Optional[int] = Column(Integer, ForeignKey("users.id"))

    replies = relationship("Comment", back_populates="parent", lazy="dynamic")

    def __repr__(self) -> str:
        return f"<Comment {self.id}>"
