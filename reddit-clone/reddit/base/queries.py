from typing import Optional

import strawberry
from strawberry.tools import create_type
from strawberry.types import Info

from reddit.base.types import NodeType


def resolve_node(info: Info, id: strawberry.ID) -> Optional[NodeType]:
    return NodeType.get_node_from_global_id(info=info, global_id=id)


node = strawberry.field(
    resolver=resolve_node,
    description="""
    Fetches an object given its ID.
    """,
)


BaseQuery = create_type(name="BaseQuery", fields=(node,))
