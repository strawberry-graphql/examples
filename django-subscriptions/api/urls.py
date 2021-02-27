from django.urls import path

from .schema import schema
from .views import AsyncGraphQLView

urlpatterns = [path("graphql", AsyncGraphQLView.as_view(schema=schema))]
