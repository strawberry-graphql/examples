# -*- coding: utf-8 -*-

import time
from typing import List, Optional

import strawberry
from asgiref.sync import sync_to_async
from django.core.serializers import deserialize, serialize
from django.db.models import Q
from strawberry_django import ModelResolver

from api import models


class HeroResolver(ModelResolver):
    model = models.Hero


# type Hero {
#   id: String
#   name: String
#   color: String!
#   updatedAt: Float
#   deleted: Boolean!
# }
class Hero(HeroResolver.output_type):
    pass


# input HeroInput {
#   id: String
#   name: String
#   color: String!
#   updatedAt: Float
#   deleted: Boolean!
# }
# The client code expects the input type to be called "HeroInput", not "CreateHero", which is the default
# We therefore need to create a new type via the strawberry.input decorator
# class HeroInput(HeroResolver.create_input_type):
@strawberry.input
class HeroInput(HeroResolver.create_input_type):
    pass


def filterHeroes(
    limit: int, id: Optional[str] = "", updatedAt: Optional[float] = -1
) -> List[Hero]:
    qs = []
    if not updatedAt:
        qs = []
    else:
        qs = [(Q(updatedAt__gt=updatedAt) | (Q(updatedAt=updatedAt) & Q(id__gt=id)))]

    return [
        Hero(
            id=h.id,
            name=h.name,
            color=h.color,
            updatedAt=h.updatedAt,
            deleted=h.deleted,
        )
        for h in models.Hero.objects.order_by("updatedAt", "id").filter(Q(*qs))[:limit]
    ]


@strawberry.type
class Query:
    ## to include the auto-generated methods from strawberry-graphql-django:
    ## - hero(id: ID!): Hero!
    ## - heros(filters: [String!] = null): [Hero!]!
    ## declare the class as
    ## class Query(HeroResolver.query()):

    # type Query {
    #   feedHero(id: String, updatedAt: Float, limit: Int!): [Hero!]!
    # }
    @strawberry.field
    async def feed_hero(
        limit: int, id: Optional[str] = "", updatedAt: Optional[float] = -1
    ) -> List[Hero]:
        return await sync_to_async(filterHeroes)(limit, id, updatedAt)


@strawberry.type
class Mutation:
    # type Mutation {
    #   setHero(hero: HeroInput): Hero
    # }
    @strawberry.mutation
    async def set_hero(self, info, hero: HeroInput = None) -> Hero:
        try:
            dhero = await sync_to_async(models.Hero.objects.get)(id=hero.id)
        except models.Hero.DoesNotExist:
            dhero = models.Hero(id=hero.id)

        dhero.color = hero.color
        dhero.name = hero.name
        dhero.updatedAt = int(time.time())
        dhero.deleted = hero.deleted

        await sync_to_async(dhero.save)()
        await info.context.broadcast.publish(
            channel="heros", message=serialize("json", [dhero])
        )

        return Hero(
            id=dhero.id,
            color=dhero.color,
            name=dhero.name,
            updatedAt=dhero.updatedAt,
            deleted=dhero.deleted,
        )


@strawberry.type
class Subscription:
    # type Subscription {
    #   changedHero(token: String!): Hero
    # }
    @strawberry.subscription
    async def changed_hero(self, info, token: str) -> Hero:
        async with info.context.broadcast.subscribe(channel="heros") as subscriber:
            async for event in subscriber:
                hero = list(deserialize("json", event.message))[0].object
                yield Hero(
                    id=hero.id,
                    color=hero.color,
                    name=hero.name,
                    updatedAt=hero.updatedAt,
                    deleted=hero.deleted,
                )


# schema {
#   query: Query
#   mutation: Mutation
#   subscription: Subscription
# }
schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
