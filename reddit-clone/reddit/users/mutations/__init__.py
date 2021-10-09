from strawberry.tools import create_type

from .authenticate import authenticate
from .avatar_remove import avatar_remove
from .email_change_request import email_change_request
from .email_change import email_change
from .password_reset_request import password_reset_request
from .password_reset import password_reset
from .user_block import user_block
from .user_create import user_create
from .user_deactivate import user_deactivate
from .user_update import user_update

UserMutation = create_type(
    name="UserMutation",
    fields=(
        authenticate,
        avatar_remove,
        email_change_request,
        email_change,
        password_reset_request,
        password_reset,
        user_block,
        user_create,
        user_deactivate,
        user_update,
    ),
)
