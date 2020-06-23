from flask_restx import fields, Namespace


class UserDto:
    """Serializer to map from single model objects to dict and viceversa.

    It also has validations in order to avoid requesting db if the request
    is not following some specific rules.

    Used for: get list of resources and post new ones.
    """

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
    """Serializer to map from single model objects to dict and viceversa.

    It also has validations in order to avoid requesting db if the request
    is not following some specific rules.

    Used for: single get, patch, delete.
    """

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
