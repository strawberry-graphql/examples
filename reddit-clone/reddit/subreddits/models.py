from typing import Optional, List

from sqlalchemy import Column, String, Integer, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base
from ..posts.models import Post


class Subreddit(Base):
    """
    Represents a Subreddit.
    """

    __tablename__ = "subreddits"

    id: Optional[int] = Column(default=None, primary_key=True)

    name: str = Column(String(75), unique=True, nullable=False)

    description: Optional[str] = Column(String(255), default=None)

    admin_id: int = Column(Integer, ForeignKey("users.id"))

    status: int = Column(SmallInteger)

    icon: Optional[str] = Column(String(255), default=None)

    posts: List[Post] = relationship("Post", back_populates="subreddit", lazy="dynamic")

    def __repr__(self) -> str:
        return f"<SubReddit {self.name}>"
