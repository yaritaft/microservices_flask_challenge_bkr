from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace("user", description="user related operations")
    user = api.model(
        "user",
        {
            "id": fields.Integer(
                required=False, description="User identifier.", readonly=True
            ),
            "name": fields.String(required=True, description="user name"),
            "age": fields.Integer(required=True, description="user age"),
            "state_id": fields.Integer(
                required=False, description="state Identifier"
            ),
            "updated_at": fields.DateTime(
                readonly=True, description="updated at date"
            ),
            "created_at": fields.DateTime(
                readonly=True, description="created at date"
            ),
        },
    )


class UserDtoDetail:
    api = Namespace("user", description="user detail related operations")
    user = api.model(
        "user",
        {
            "id": fields.Integer(
                required=False, description="User identifier.", readonly=True
            ),
            "name": fields.String(required=False, description="user name"),
            "age": fields.Integer(required=False, description="user age"),
            "state_id": fields.Integer(
                required=False, description="state Identifier"
            ),
            "updated_at": fields.DateTime(
                required=False, readonly=True, description="updated at date"
            ),
            "created_at": fields.DateTime(
                required=False, readonly=True, description="created at date"
            ),
        },
    )
