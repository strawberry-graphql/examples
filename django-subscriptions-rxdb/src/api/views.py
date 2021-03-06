# -*- coding: utf-8 -*-

import os

import strawberry
from django.http import Http404, HttpRequest
from django.template import RequestContext, Template
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from strawberry.django.views import AsyncGraphQLView as StrawberryAsyncGraphQLView

from .context import Context, get_broadcast


class AsyncGraphQLView(StrawberryAsyncGraphQLView):
    async def get_context(self, request: HttpRequest) -> Context:
        broadcast = await get_broadcast()

        return Context(broadcast)

    def _render_graphiql(self, request: HttpRequest, context=None):
        if not self.graphiql:
            raise Http404()

        try:
            template = Template(render_to_string("graphql/graphiql.html"))
        except TemplateDoesNotExist:
            template = Template(
                open(
                    os.path.join(
                        os.path.dirname(os.path.abspath(strawberry.__file__)),
                        "static/graphiql.html",
                    ),
                    "r",
                ).read()
            )

        context = context or {}
        # THIS enables subscriptions
        context.update({"SUBSCRIPTION_ENABLED": "true"})

        response = TemplateResponse(request=request, template=None, context=context)
        response.content = template.render(RequestContext(request, context))

        return response
