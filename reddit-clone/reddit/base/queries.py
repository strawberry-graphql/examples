from typing import Optional

from strawberry import field, type, ID
from strawberry.types import Info

from reddit.base.types import NodeType


@type
class BaseQueries:
    @field(name="node", description="Fetches an object given its ID.")
    def resolve_node(self, info: Info, id: ID) -> Optional[NodeType]:
        return NodeType.get_node_from_global_id(info=info, global_id=id)
