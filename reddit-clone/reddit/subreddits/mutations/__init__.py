from strawberry.tools import create_type

from .subreddit_create import subreddit_create

SubredditMutation = create_type(name="SubredditMutation", fields=(subreddit_create,))
