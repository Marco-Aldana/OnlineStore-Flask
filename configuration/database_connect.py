"""

"""
# ---------------------------------------------------------------------------------------------------------------Imports
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask import g

from configuration.constants import SERVER, USER, PASSWORD, DB
from repositories.databases.models import metadata


# ---------------------------------------------------------------------------------------Open Connection to the Database
def database_connection_alchemy():
    if not getattr(g, "db_connection", None):
        g.engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{SERVER}/{DB}?charset=utf8mb4", echo=True)
    return g.engine


# -----------------------------------------------------------------------------------Create the database if it's not set
def init_database():
    engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{SERVER}/{DB}?charset=utf8mb4", echo=True)
    if not database_exists(engine.url):
        create_database(engine.url)
    else:

        metadata.create_all(g.engine)
# ----------------------------------------