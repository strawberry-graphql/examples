from strawberry.django.views import AsyncGraphQLView as BaseAsyncGraphQLView


class AsyncGraphQLView(BaseAsyncGraphQLView):
    async def get_context(self, request, response):
        return {
            "request": request,
            "response": response,
            "dataloaders": {},
        }
