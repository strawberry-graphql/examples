from strawberry.tools import create_type

from .post_create import post_create
from .post_delete import post_delete
from .post_update import post_update
from .post_vote import post_vote

PostMutation = create_type(
    name="PostMutation", fields=(post_create, post_delete, post_update, post_vote)
)
