from typing import Optional

import strawberry
from strawberry.types import Info

from reddit.base.types import NodeType


@strawberry.type
class BaseQuery:
    @strawberry.field(name="node", description="Fetches an object given its ID.")
    def resolve_node(self, info: Info, id: strawberry.ID) -> Optional[NodeType]:
        return NodeType.get_node_from_global_id(info=info, global_id=id)
