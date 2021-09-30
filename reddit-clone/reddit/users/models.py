from typing import Optional, List

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base
from ..comments.models import Comment
from ..subreddits.models import Subreddit
from ..posts.models import Post


class User(Base):
    """
    Represents an individual user account.
    """

    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, nullable=False)

    username: str = Column(String(32), nullable=False, unique=True)

    email: str = Column(String(255), nullable=False, unique=True)

    password: str = Column(String(255), nullable=False)

    avatar: Optional[str] = Column(String(255), default=None)

    posts: List[Post] = relationship("Post", back_populates="user", lazy="dynamic")

    subreddits: List[Subreddit] = relationship(
        "Subreddit", back_populates="user", secondary="subreddit_users", lazy="dynamic"
    )

    comments: List[Comment] = relationship(
        "Comment", back_populates="user", lazy="dynamic"
    )

    def __repr__(self) -> str:
        return f"<User {self.username}>"


class SubredditUser(Base):
    """
    Represents a Subreddit-user relationship.
    """

    __tablename__ = "subreddit_users"

    user_id: int = Column(Integer, ForeignKey("users.id"), primary_key=True)

    subreddit_id: int = Column(Integer, ForeignKey("subreddits.id"), primary_key=True)

    def __repr__(self) -> str:
        return f"<Subreddit User {self.user_id}>"
