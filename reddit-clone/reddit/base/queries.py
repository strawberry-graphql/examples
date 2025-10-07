from typing import Optional

import strawberry
from strawberry.tools import create_type
from strawberry.types import Info
from graphql_relay import from_global_id

from reddit.base.types import NodeType


def resolve_node(info: Info, id: strawberry.ID) -> Optional[NodeType]:
    try:
        type_name, _id = from_global_id(id)
    except Exception:
        raise Exception(f'Unable to parse global ID "{id}".')

    schema_type = info.schema.get_type_by_name(type_name)
    if schema_type is None:
        raise Exception(f'Relay Node "{type_name}" not found in schema')

    # We make sure the ObjectType implements the "Node" interface
    if NodeType not in schema_type._type_definition.interfaces:
        raise Exception(
            f'ObjectType "{type_name}" does not implement the "{NodeType}" interface.'
        )

    resolver = getattr(schema_type, "resolve_node", None)
    if resolver is not None:
        return resolver(info, _id)


node = strawberry.field(
    resolver=resolve_node,
    description="""
    Fetches an object given its ID.
    """,
)


BaseQuery = create_type(name="BaseQuery", fields=(node,))
