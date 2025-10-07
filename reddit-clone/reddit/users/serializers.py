from marshmallow import Schema, pre_load
from marshmallow.fields import String, Integer, Boolean
from marshmallow.validate import Email, Length


__all__ = ("user_schema",)


class UserSchema(Schema):
    id = Integer(dump_only=True)
    email = String(
        required=True,
        validate=Email(
            error="Not a valid email address.",
        ),
    )
    username = String(
        required=True,
        validate=(Length(min=2, max=32),),
    )
    password = String(
        required=True,
        load_only=True,
        validate=(Length(min=8),),
    )
    avatar = String(dump_only=True)
    is_active = Boolean(dump_only=True)

    def process_input(self, data, **kwargs):
        # clean user emails before storing them.
        data["email"] = data["email"].lower().strip()
        return data

    pre_load(process_input)


user_schema = UserSchema()
