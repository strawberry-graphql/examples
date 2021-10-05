from strawberry import type, field, ID


@type(name="Node", description="An object with an ID.")
class NodeType:
    id: ID = field(
        description="""
        ID of the object.
        """
    )
