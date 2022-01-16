from marshmallow import Schema, fields, validate


class BaseSchema(Schema):
    class Meta:
        datetimeformat = '%Y-%m-%d %H:%M:%S'
        load_only = ["password"]
        ordered = True
        unknown = "RAISE"


class UserCreateRequestSchema(BaseSchema):
    username = fields.String(required=True, validate=validate.Length(min=3, max=20))
    full_name = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8))


class UserResponseSchema(BaseSchema):
    id = fields.Integer(required=True)
    username = fields.String(required=True, validate=validate.Length(min=3, max=20))
    full_name = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8))
    image = fields.String(required=False)
    is_active = fields.Boolean()
    is_validated = fields.Boolean()
    created_at = fields.DateTime()
