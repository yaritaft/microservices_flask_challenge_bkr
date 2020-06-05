from marshmallow import Schema, fields


class StateSchemaCreation(Schema):
    id = fields.Int(required=True)
    code = fields.Int(required=True)
    name = fields.Str(required=True)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)


class StateSchemaDetail(Schema):
    id = fields.Int(required=True)
    code = fields.Int(required=False)
    name = fields.Str(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
