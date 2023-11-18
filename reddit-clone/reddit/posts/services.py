from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from reddit.users.models import User
from reddit.posts.models import Post


async def create_post(
    session: AsyncSession,
    title: str,
    owner_id: int,
    subreddit_id: int,
    link: Optional[str] = None,
    text: Optional[str] = None,
) -> Post:
    """
    Creates a new post instance.
    """
    post = Post(
        title=title, text=text, link=link, owner_id=owner_id, subreddit_id=subreddit_id
    )
    # TODO: validate input data here.
    session.add(instance=post)
    await session.commit()
    await session.refresh(instance=post)
    return post


async def vote_post(session: AsyncSession, post: Post, user: User) -> Post:
    """
    Creates a vote on the given post.
    """


async def update_post(session: AsyncSession, post: Post) -> Post:
    """
    Updates the given post instance.
    """


async def delete_post(session: AsyncSession, post: Post, user: User) -> Post:
    """
    Deletes the given post instance.
    """
