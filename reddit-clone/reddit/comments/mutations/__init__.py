from strawberry.tools import create_type

from .comment_create import comment_create
from .comment_delete import comment_delete
from .comment_update import comment_update
from .comment_vote import comment_vote

CommentMutation = create_type(
    name="CommentMutation",
    fields=(comment_create, comment_delete, comment_update, comment_vote),
)
