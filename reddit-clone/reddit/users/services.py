from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from reddit.users.models import User


async def authenticate(
    session: AsyncSession, username: str, password: str
) -> Optional[User]:
    """
    Checks if the provided user credentials are valid.
    """
    user = await User.by_username(session=session, username=username)
    if user is None or not user.check_password(password=password):
        # TODO: handle exception here.
        pass
    return user


async def create_user(
    session: AsyncSession, email: str, username: str, password: str
) -> User:
    """
    Creates a new user instance.
    """
    user = User(email=email, username=username)
    user.set_password(password=password)
    # TODO: validate input data here.
    session.add(instance=user)
    await session.commit()
    await session.refresh(instance=user)
    return user


async def update_user(session: AsyncSession, user: User):
    """
    Updates the given user instance.
    """


async def remove_avatar(session: AsyncSession, user: User) -> User:
    """
    Removes the avatar for the given user instance.
    """
    user.avatar = None
    session.add(instance=user)
    await session.commit()
    await session.refresh(instance=user)
    return user


async def request_change_email(session: AsyncSession, email: str, password: str):
    """
    Sends an email change code to the user's new email.
    """


async def change_email(
    session: AsyncSession, email: str, change_code: str, password: str
):
    """
    Changes the email for the given user instance.
    """


async def request_reset_password(session: AsyncSession, email: str):
    """
    Sends a password reset code to the given email, if it
    actually exists.
    """


async def reset_password(
    session: AsyncSession, password: str, reset_code: str, email: str
):
    """
    Resets the password for the given user instance.
    """


async def block_user(session: AsyncSession, user_id: int, user: User):
    """
    Blocks the user account for the given user instance.
    """


async def deactivate_user(session: AsyncSession, password: str, user: User) -> User:
    """
    Deactivates the given user instance.
    """
    if not user.check_password(password=password):
        # TODO: handle exception here.
        pass
    user.is_active = False
    session.add(instance=user)
    await session.commit()
    await session.refresh(instance=user)
    return user
