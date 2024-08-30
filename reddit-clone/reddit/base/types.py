from __future__ import annotations

from typing import Generic, List, Optional, TypeVar

import strawberry


@strawberry.interface(name="Node", description="An object with an ID.")
class NodeType:
    # TODO: need to make custom ID resolver
    id: strawberry.ID = strawberry.field(
        description="""
        ID of the object.
        """
    )


Node = TypeVar(name="Node")

Cursor = TypeVar(name="Cursor")

Edge = TypeVar(name="Edge")


# TODO: make an abstract type
@strawberry.type(name="Edge")
class EdgeType(Generic[Node, Cursor]):
    cursor: Cursor = strawberry.field(
        description="""
        A cursor for use in pagination.
        """
    )

    node: NodeType = strawberry.field(
        description="""
        The item at the end of the edge.
        """
    )


@strawberry.type(name="PageInfo")
class PageInfoType(Generic[Cursor]):
    end_cursor: Optional[Cursor] = strawberry.field(
        description="""
        When paginating forwards, the cursor to continue.
        """
    )

    has_next_page: bool = strawberry.field(
        description="""
        When paginating forwards, are there more items?
        """
    )

    has_previous_page: bool = strawberry.field(
        description="""
        When paginating backwards, are there more items?
        """
    )

    start_cursor: Optional[Cursor] = strawberry.field(
        description="""
        When paginating backwards, the cursor to continue.
        """
    )


# TODO: make an abstract type
@strawberry.type(name="Connection")
class ConnectionType(Generic[Node, Edge]):
    edges: List[Edge] = strawberry.field(
        description="""
        Contains the edges in the connection.
        """
    )

    nodes: List[Node] = strawberry.field(
        description="""
        Contains the nodes in the connection.
        """
    )

    page_info: PageInfoType = strawberry.field(
        description="""
        Information to aid in pagination.
        """
    )

    total_count: int = strawberry.field(
        description="""
        Identifies the total count of items in the connection.
        """
    )
