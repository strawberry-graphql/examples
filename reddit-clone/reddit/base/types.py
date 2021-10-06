from strawberry import type, field, ID
from strawberry.types import Info
from graphql_relay import from_global_id, to_global_id


@type(name="Node", description="An object with an ID.")
class NodeType:
    id: ID = field(
        description="""
        ID of the object.
        """
    )

    @classmethod
    def get_node_from_global_id(cls, info: Info, global_id: str, only_type=None):
        try:
            _type, _id = cls.from_global_id(global_id)
        except Exception as e:
            raise Exception(
                f'Unable to parse global ID "{global_id}". '
                'Make sure it is a base64 encoded string in the format: "TypeName:id". '
                f"Exception message: {str(e)}"
            )

        info.schema.get_type(_type)

    @classmethod
    def from_global_id(cls, global_id: str):
        return from_global_id(global_id)

    @classmethod
    def to_global_id(cls, schema_type: str, id: str):
        return to_global_id(schema_type, id)
