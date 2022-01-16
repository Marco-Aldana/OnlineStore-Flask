from flask import jsonify, request
from marshmallow import ValidationError
from project.repositories.users_repository import create_user_repository
from project.schemas.user_models import UserResponseSchema, UserCreateRequestSchema


# Users routes ---------------------------------------------------------------------------------------------------------
def get_users_route():
    return jsonify("hi")


def create_user_route():
    try:
        body_request = UserCreateRequestSchema().load(request.get_json())  # validation input
        user = create_user_repository(body_request)  # calling method
        return user
        # return UserResponseSchema().dump(user)  # validation response
    except ValidationError as err:
        return err.messages  # print if error


"""
    try:
        body_request = UserCreateRequestSchema().load(request.get_json())  # validation input
        user = create_user_repository(body_request)  # calling method
        return UserResponseSchema().dump(user)  # validation response
    except ValidationError as err:
        return err.messages  # print if error
"""


def get_user_by_id_route(id_user):
    try:
        user = create_user_repository(id_user)  # calling method
        return UserResponseSchema().dump(user)  # validation response
    except ValidationError as err:
        return err.messages  # print if error


def edit_user_route(id_user):
    return jsonify({"description": f"This method will edit an user {id_user}"})


def delete_user_route(id_user):
    return jsonify({"description": f"This method will delete an user {id_user}"})
