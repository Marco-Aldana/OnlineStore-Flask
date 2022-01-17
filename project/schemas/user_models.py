import re
from typing import BinaryIO

from marshmallow import Schema, fields, validate, validates, ValidationError, validates_schema

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

    @validates_schema
    def validate_types(self, data, **kwargs):
        if data.get('attribute') in ['username', 'full_name', 'password', 'image']:
            if type(data.get('value')) != str:
                raise ValidationError("The value must be 'str' type")
        if data.get('attribute') in ['email']:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not re.fullmatch(regex, data.get('value')):
                raise ValidationError("The value must be 'email' type")
        if data.get('attribute') in ['is_active', 'is_validated']:
            if data.get('value') < 0 or data.get('value') > 1:
                raise ValidationError("The value must be 1 or 0")
