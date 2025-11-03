from strawberry.tools import create_type

from .mutations.register_user import register_user
from .mutations.login_user import login_user


Mutation = create_type(
    "Mutation",
    [
        register_user,
        login_user,
    ],
)
