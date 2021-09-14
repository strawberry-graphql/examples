from strawberry.django.views import AsyncGraphQLView
from django.urls import path

from .schema import schema

urlpatterns = [
    path(
        "graphql/",
        AsyncGraphQLView.as_view(schema=schema),
    ),
]
