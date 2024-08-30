from typing import Optional, List

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base
from ..posts.models import Post


class Subreddit(Base):
    """
    Represents a Subreddit.
    """

    __tablename__ = "subreddits"

    id: int = Column(Integer, primary_key=True, nullable=False)

    name: str = Column(String(75), unique=True, nullable=False)

    description: Optional[str] = Column(String(255), default=None)

    owner_id: int = Column(Integer, ForeignKey("users.id"))

    icon: Optional[str] = Column(String(255), default=None)

    posts: List[Post] = relationship("Post", back_populates="subreddit", lazy="dynamic")

    def __repr__(self) -> str:
        return f"<SubReddit {self.name}>"
