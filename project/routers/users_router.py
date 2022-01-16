from typing import List

from flask import request
from marshmallow import ValidationError

from project.repositories.users_repository import create_user_repository, get_user_by_id_repository, \
    get_users_repository, edit_user_repository, delete_user_repository
from project.schemas.user_models import UserResponseSchema, UserCreateRequestSchema, UserParametersSchema


# Users routes ---------------------------------------------------------------------------------------------------------
def get_users_route() -> List[UserResponseSchema]:
    try:
        users_list = get_users_repository()  # calling method
        user_data_list = [user.__repr__() for user in users_list]
        return UserResponseSchema().load(user_data_list, many=True)  # validation response
    except ValidationError as err:
        return err.messages  # send validation error


def create_user_route() -> UserResponseSchema:
    try:
        body_request = UserCreateRequestSchema().load(request.get_json())  # validation input
        user = create_user_repository(body_request)  # calling method
        return UserResponseSchema().load(user.__repr__())  # validation response
    except ValidationError as err:
        return err.messages  # send validation error


def get_user_by_id_route(id_user: int) -> UserResponseSchema:
    try:
        user = get_user_by_id_repository(id_user)  # calling method
        return UserResponseSchema().load(user.__repr__())  # validate output
    except ValidationError as err:
        return err.messages  # send validation error


def edit_user_route(id_user: int) -> UserResponseSchema:
    """
    The input format in body must be a list of dicts and be like:
    [{"attribute": value, "value": value},]

    The attribute must be a valid parameter in the Object Model to edit
    :param id_user: int
    :return: user dict
    """
    try:
        parameters = UserParametersSchema().load(request.get_json(), many=True)  # loading parameters to edit
        user = edit_user_repository(id_user, parameters)  # calling repository method
        return UserResponseSchema().load(user.__repr__())  # validate output
    except ValidationError as err:
        return err.messages  # send validation error


def delete_user_route(id_user: int) -> UserResponseSchema:
    try:
        user = delete_user_repository(id_user)
        return UserResponseSchema().load(user.__repr__())
    except ValidationError as err:
        return err.messages  # send validation error
