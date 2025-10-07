from sqlalchemy.ext.asyncio import AsyncSession

from reddit.users.models import User
from reddit.comments.models import Comment


async def create_comment(
    session: AsyncSession, content: str, owner_id: int, post_id: int
) -> Comment:
    """
    Creates a new comment instance.
    """
    comment = Comment(content=content, owner_id=owner_id, post_id=post_id)
    # TODO: validate input data here.
    session.add(instance=comment)
    await session.commit()
    await session.refresh(instance=comment)
    return comment


async def vote_comment(session: AsyncSession, comment: Comment, user: User) -> Comment:
    """
    Creates a vote on the given comment.
    """


async def update_comment(session: AsyncSession, comment: Comment) -> Comment:
    """
    Updates the given comment instance.
    """


async def delete_comment(
    session: AsyncSession, comment: Comment, user: User
) -> Comment:
    """
    Deletes the given comment instance.
    """
