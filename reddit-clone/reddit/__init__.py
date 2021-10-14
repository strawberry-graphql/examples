from typing import Union, Optional, Any

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.dataloader import DataLoader
from strawberry.asgi import GraphQL

from reddit import settings
from reddit.schema import schema
from reddit.users.loaders import load_users
from reddit.subreddits.loaders import load_subreddits
from reddit.posts.loaders import load_posts
from reddit.comments.loaders import load_comments

__all__ = ("app",)


class MyGraphQL(GraphQL):
    async def get_context(
        self, request: Union[Request, WebSocket], response: Optional[Response] = None
    ) -> Optional[Any]:
        context: dict = await super().get_context(request, response=response)
        context.update(
            user_loader=DataLoader(load_fn=load_users),
            subreddit_loader=DataLoader(load_fn=load_subreddits),
            post_loader=DataLoader(load_fn=load_posts),
            comment_loader=DataLoader(load_fn=load_comments),
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
