from flask_restplus import fields, Namespace


class StateDto:
    """Serializer to map from single model objects to dict and viceversa.

    It also has validations in order to avoid requesting db if the request
    is not following some specific rules.

    Used for: get list of resources and post new ones.
    """

    api = Namespace("state", description="state related operations")
    state = api.model(
        "state",
        {
            "id": fields.Integer(
                required=False, description="state identifier.", readonly=True
            ),
            "name": fields.String(required=True, description="state name"),
            "code": fields.Integer(required=True, description="state code"),
            "updated_at": fields.DateTime(
                readonly=True, description="updated at date"
            ),
            "created_at": fields.DateTime(
                readonly=True, description="created at date"
            ),
        },
    )


class StateDtoDetail:
    """Serializer to map from single model objects to dict and viceversa.

    It also has validations in order to avoid requesting db if the request
    is not following some specific rules.

    Used for: single get, patch, delete.
    """

    api = Namespace("state", description="state detail related operations")
    state = api.model(
        "state",
        {
            "id": fields.Integer(
                required=False, description="state identifier.", readonly=True
            ),
            "name": fields.String(required=False, description="state name"),
            "code": fields.Integer(required=False, description="state code"),
            "updated_at": fields.DateTime(
                required=False, readonly=True, description="updated at date"
            ),
            "created_at": fields.DateTime(
                required=False, readonly=True, description="created at date"
            ),
        },
    )
