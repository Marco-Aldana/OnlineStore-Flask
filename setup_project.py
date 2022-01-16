from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from project import db
from project.config import SQLALCHEMY_DATABASE_URI


def setup_database():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url):
        create_database(engine.url)
    db.create_all()