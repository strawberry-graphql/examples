from typing import Optional

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from sqlalchemy import select

from reddit.base.services import BaseService
from reddit.users.models import User


class UserService(BaseService):
    _hasher = PasswordHasher()

    async def create_user(self, username: str, password: str, email: str) -> User:
        """
        Creates an user instance.
        """
        # TODO: validate input before creating
        user = User(
            email=email,
            username=username,
            password=self._hasher.hash(password=password),
        )
        self._session.add(instance=user)
        await self._session.commit()
        await self._session.refresh(instance=user)
        return user

    async def get_by_username(self, username: str) -> Optional[User]:
        """
        Gets an user by their username.
        """
        stmt = select(User).filter_by(username=username).first()
        return await self._session.execute(stmt)

    async def authenticate(self, username: str, password: str) -> Optional[User]:
        """
        Checks whether the given credentials match
        and returns the associated user instance.
        """
        user = self.get_by_username(username=username)
        if user is None:
            return user
        try:
            self._hasher.verify(hash=user.password, password=password)
        except VerifyMismatchError:
            return None

        if self._hasher.check_needs_rehash(hash=user.password):
            # recalculate the user's password hash.
            user.password = self._hasher.hash(password=password)
            self._session.add(instance=user)
            await self._session.commit()
            await self._session.refresh(instance=user)
        return user
