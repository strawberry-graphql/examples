from strawberry.tools import create_type

from .subreddit_create import subreddit_create
from .subreddit_delete import subreddit_delete
from .subreddit_join import subreddit_join
from .subreddit_leave import subreddit_leave
from .subreddit_update import subreddit_update

SubredditMutation = create_type(
    name="SubredditMutation",
    fields=(
        subreddit_create,
        subreddit_delete,
        subreddit_join,
        subreddit_leave,
        subreddit_update,
    ),
)
