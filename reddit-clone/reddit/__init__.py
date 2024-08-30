from typing import Union, Optional, Any

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.dataloader import DataLoader
from strawberry.asgi import GraphQL

from reddit import settings
from reddit.schema import schema
from reddit.users.loaders import load_users_by_id, load_users_by_username
from reddit.subreddits.loaders import load_subreddits_by_id
from reddit.posts.loaders import load_posts_by_id
from reddit.comments.loaders import load_comments_by_id

__all__ = ("app",)


class MyGraphQL(GraphQL):
    async def get_context(
        self, request: Union[Request, WebSocket], response: Optional[Response] = None
    ) -> Optional[Any]:
        context = await super().get_context(request, response=response)
        context.update(
            user_id_loader=DataLoader(load_fn=load_users_by_id),
            user_username_loader=DataLoader(load_fn=load_users_by_username),
            subreddit_id_loader=DataLoader(load_fn=load_subreddits_by_id),
            post_id_loader=DataLoader(load_fn=load_posts_by_id),
            comment_id_loader=DataLoader(load_fn=load_comments_by_id),
        )
        return context


def create_application() -> Starlette:
    """
    Creates an application instance.

    :return: The created application.
    """
    app = Starlette(debug=settings.DEBUG)
    graphql_app = MyGraphQL(schema=schema, graphiql=True, debug=settings.DEBUG)
    app.add_route(
        path="/graphql",
        route=graphql_app,
    )

    return app


app = create_application()
