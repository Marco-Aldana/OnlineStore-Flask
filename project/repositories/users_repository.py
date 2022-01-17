from flask import abort

from .. import db
from ..schemas.database_models import UsersTable
from ..schemas.user_models import UserCreateRequestSchema, UserParametersSchema


def create_user_repository(user_data: UserCreateRequestSchema()):
    if UsersTable.query.filter_by(username=user_data['username']).first():
        abort(409, description="Username in use")
    if UsersTable.query.filter_by(email=user_data['email']).first():
        abort(409, description="Email in Use")

    user = UsersTable(
        username=user_data['username'],
        full_name=user_data['full_name'],
        email=user_data['email'],
        password=user_data['password']
    )
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_id_repository(id_user):
    user = UsersTable.query.get(id_user)
    if user:
        return user
    else:
        abort(404, description="User not found")


def get_users_repository():
    users_list = UsersTable.query.all()
    return users_list


def edit_user_repository(id_user, parameters):
    user = get_user_by_id_repository(id_user)  # calling the user

    for parameter in parameters:

        attribute = parameter.get('attribute')
        value = parameter.get('value')
        if attribute == 'username':
            if UsersTable.query.filter_by(username=value).first():
                abort(409, description="Username in use")
        if attribute == 'email':
            if UsersTable.query.filter_by(email=value).first():
                abort(409, description="Email in use")

        user.__setattr__(attribute, value)
        print(f'{parameter.get("attribute")} was requested to modified')

    db.session.merge(user)
    db.session.commit()
    return user


def delete_user_repository(id_user):
    user = get_user_by_id_repository(id_user)  # calling the user
    db.session.delete(user)
    db.session.commit()
    return user
