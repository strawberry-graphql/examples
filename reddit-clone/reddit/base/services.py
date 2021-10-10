from sqlalchemy.ext.asyncio.session import AsyncSession


class BaseService:
    """
    The base class that every service must subclass.
    Services are classes which implement business logic
    and improve code reusability.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
