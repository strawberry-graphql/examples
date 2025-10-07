from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from reddit.users.models import User
from reddit.subreddits.models import Subreddit


async def create_subreddit(
    session: AsyncSession, owner_id: int, name: str, description: Optional[str] = None
) -> Subreddit:
    """
    Creates a new subreddit instance.
    """
    subreddit = Subreddit(name=name, description=description, owner_id=owner_id)
    # TODO: validate input data here.
    session.add(instance=subreddit)
    await session.commit()
    await session.refresh(instance=subreddit)
    return subreddit


async def update_subreddit(session: AsyncSession, subreddit: Subreddit) -> Subreddit:
    """
    Updates the given subreddit instance.
    """


async def delete_subreddit(
    session: AsyncSession, subreddit: Subreddit, user: User
) -> Subreddit:
    """
    Deletes the given subreddit instance.
    """
