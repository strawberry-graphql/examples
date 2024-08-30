from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from reddit.users.models import User


async def user_by_email(session: AsyncSession, email: str) -> Optional[User]:
    """
    Gets an user by their email.
    """
    query = select(User).filter(User.email == email)
    return (await session.execute(query)).scalar_one()


async def user_by_username(session: AsyncSession, username: str) -> Optional[User]:
    """
    Gets an user by their username.
    """
    query = select(User).filter(User.username == username)
    return (await session.execute(query)).scalar_one()


async def authenticate(
    session: AsyncSession, username: str, password: str
) -> Optional[User]:
    """
    Checks if the provided user credentials are valid.
    """
    user = await user_by_username(session=session, username=username)
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


async def update_user(session: AsyncSession, user: User) -> User:
    """
    Updates the given user instance.
    """


async def remove_user_avatar(session: AsyncSession, user: User) -> User:
    """
    Removes the avatar for the given user instance.
    """
    user.avatar = None
    session.add(instance=user)
    await session.commit()
    await session.refresh(instance=user)
    return user


async def request_change_email(
    session: AsyncSession, email: str, password: str, user: User
):
    """
    Sends an email change code to the user's new email.
    """
    if not user.check_password(password=password):
        # TODO: handle exception here.
        pass
    user = await user_by_email(session=session, email=email)
    if user is not None:
        # TODO: handle exception here.
        pass
    # TODO: store email change code and send
    # change request email.


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
    user = await user_by_email(session=session, email=email)
    if user is not None:
        # TODO: store password reset code and
        # send password reset email here.
        pass


async def reset_password(
    session: AsyncSession, password: str, reset_code: str, email: str
):
    """
    Resets the password for the given user instance.
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
