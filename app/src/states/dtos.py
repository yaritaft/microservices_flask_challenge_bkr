from flask_restplus import Namespace, fields


class StateDto:
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
