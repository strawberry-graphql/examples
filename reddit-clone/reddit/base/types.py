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
    def resolve(
        cls, info: Info, global_id: str, only_type=None
    ) -> Optional[Type[NodeType]]:
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

        if only_type:
            assert schema_type == only_type

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
    cursor: str
    node: NodeType


@strawberry.type(name="PageInfo")
class PageInfoType:
    end_cursor: Optional[str]
    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str]


@strawberry.type(name="Connection")
class ConnectionType:
    edges: List[EdgeType]
    nodes: List[NodeType]
    page_info: PageInfoType
    total_count: int
