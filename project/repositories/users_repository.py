import datetime

from flask import g
from sqlalchemy.orm import Session
from flask import request, jsonify
from sqlalchemy import select
from marshmallow import ValidationError

from .. import db
from ..schemas.database_models import UsersTable
from ..schemas.user_models import UserCreateRequestSchema, UserResponseSchema


def create_user_repository(user_data: UserCreateRequestSchema()):
    user = UsersTable.query.get(1)

    if user:
        return user.__repr__()

    user = UsersTable(
        username=user_data['username'],
        full_name=user_data['full_name'],
        email=user_data['email'],
        password=user_data['password']
    )
    db.session.add(user)
    db.session.commit()

    return user.__repr__()


"""    user["id"] = 1
    user["image"] = "no image"
    user["dummy"] = 33
    user["is_active"] = True
    user["is_validated"] = False
    user["created_at"] = datetime.datetime.now()

    with g.engine.begin() as connection:
        search_username = connection.execute(select([users_table]).where(users_table.c.username == user["username"]))
        exist_username=search_username.fetchall()

        if exist_username:
            raise ValidationError("the username exists")

        search_email = connection.execute(select([users_table]).where(users_table.c.email == user["email"]))
        exist_email = search_email.fetchall()

        if exist_email:
            raise ValidationError("the email exists")

        _query = users_table.insert().values(
            username=user["username"],
            password=user["password"],
            email=user["email"],
            full_name=user["full_name"]
        )
        result=connection.execute(_query)
        result=result.fetchall()
        session = Session(g.engine)
        session.commit()
        print("----------------------------------------------------------------------------------")
        print(result)
        print("----------------------------------------------------------------------------------")
        session.close()

    return user
"""

""" with g.engine.begin() as connection:
        sql_request = users_table.insert().values()
        sql_result = connection.execute(sql_request)
        session = Session(g.engine)
        session.commit()
        session.close()
        response = sql_result.fetchall()"""
