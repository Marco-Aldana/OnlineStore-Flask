from marshmallow import Schema, fields, validate

from project.schemas.database_models import UsersTable


class BaseMeta:
    datetimeformat = '%Y-%m-%d %H:%M:%S'
    load_only = ["password"]
    ordered = True
    unknown = "RAISE"


class UserCreateRequestSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3, max=20))
    full_name = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8))

    class Meta(BaseMeta):
        pass


class UserResponseSchema(Schema):
    id = fields.Integer(required=True)
    username = fields.String(required=True, validate=validate.Length(min=3, max=20))
    full_name = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    image = fields.String(required=False)

    class Meta(BaseMeta):
        pass


class UserParametersSchema(Schema):
    attribute = fields.String(required=True, validate=validate.OneOf(UsersTable.get_attributes()))
    value = fields.Field(required=True)

    class Meta(BaseMeta):
        pass
