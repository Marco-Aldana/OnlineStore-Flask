import connexion
from flask_sqlalchemy import SQLAlchemy

app_connexion = connexion.FlaskApp("online-store", specification_dir="./")
app = app_connexion.app
app.config.from_object('project.config')
db = SQLAlchemy(app)
app_connexion.add_api("openapi.yml")
