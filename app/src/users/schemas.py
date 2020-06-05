from marshmallow import fields, Schema


class UserSchemaCreation(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    state_id = fields.Int(required=True)


class UserSchemaDetail(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=False)
    age = fields.Int(required=False)
    state_id = fields.Int(required=False)
