from __future__ import annotations

from typing import List, Optional

import strawberry


@strawberry.interface(name="Node", description="An object with an ID.")
class NodeType:
    id: strawberry.ID = strawberry.field(
        description="""
        ID of the object.
        """
    )


@strawberry.type(name="Edge")
class EdgeType:
    cursor: str = strawberry.field(
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
class PageInfoType:
    end_cursor: Optional[str] = strawberry.field(
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

    start_cursor: Optional[str] = strawberry.field(
        description="""
        When paginating backwards, the cursor to continue.
        """
    )


@strawberry.type(name="Connection")
class ConnectionType:
    edges: List[EdgeType] = strawberry.field(
        description="""
        Contains the edges in the connection.
        """
    )

    nodes: List[NodeType] = strawberry.field(
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
