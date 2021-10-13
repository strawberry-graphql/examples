from __future__ import annotations

from typing import List, Optional, Type

import strawberry
from strawberry.types import Info
from graphql_relay import from_global_id, to_global_id


@strawberry.interface(name="Node", description="An object with an ID.")
class NodeType:
    id: strawberry.ID = strawberry.field(
        description="""
        ID of the object.
        """
    )

    @classmethod
    def resolve(cls, info: Info, global_id: str) -> Optional[Type[NodeType]]:
        try:
            type_name, _id = cls.from_global_id(global_id)
        except Exception as e:
            raise Exception(
                f'Unable to parse global ID "{global_id}". '
                f"Exception message: {str(e)}"
            )

        schema_type = info.schema.get_type_by_name(type_name)
        if schema_type is None:
            raise Exception(f'Relay Node "{type_name}" not found in schema')

        # We make sure the ObjectType implements the "Node" interface
        if cls not in schema_type._type_definition.interfaces:
            raise Exception(
                f'ObjectType "{type_name}" does not implement the "{cls}" interface.'
            )

        resolver = getattr(schema_type, "resolve_node", None)
        if resolver is not None:
            return resolver(info, _id)

    @classmethod
    def from_global_id(cls, global_id: str):
        return from_global_id(global_id)

    @classmethod
    def to_global_id(cls, schema_type: str, id: str) -> str:
        return to_global_id(schema_type, id)


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
