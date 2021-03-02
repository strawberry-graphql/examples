# -*- coding: utf-8 -*-

import asyncio
import time
import traceback
from typing import List, Optional

import django.core.serializers
import strawberry
from asgiref.sync import sync_to_async
from django.db.models import Q

from api import models


# input HeroInput {
#   id: String
#   name: String
#   color: String!
#   updatedAt: Float
#   deleted: Boolean!
# }
@strawberry.input
class HeroInput:
    id: str
    color: str
    name: Optional[str] = ""
    updatedAt: Optional[float] = 0
    deleted: Optional[bool] = False


# type Hero {
#   id: String
#   name: String
#   color: String!
#   updatedAt: Float
#   deleted: Boolean!
# }
@strawberry.type
class Hero:
    id: str
    color: str
    name: Optional[str] = ""
    updatedAt: Optional[float] = 0
    deleted: Optional[bool] = False


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
    @strawberry.field
    def hello() -> str:
        return "world"

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
        print(f"Creating Hero from HeroInput {hero}")

        shero = Hero(
            id=hero.id,
            color=hero.color,
            name=hero.name,
            updatedAt=hero.updatedAt,
            deleted=hero.deleted,
        )
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
            channel="heros", message=django.core.serializers.serialize("json", [dhero])
        )

        return shero


@strawberry.type
class Subscription:
    # type Subscription {
    #   changedHero(token: String!): Hero
    # }
    @strawberry.subscription
    async def changed_hero(self, info, token: str) -> Hero:
        async with info.context.broadcast.subscribe(channel="heros") as subscriber:
            async for event in subscriber:
                hero = list(django.core.serializers.deserialize("json", event.message))[
                    0
                ].object
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
