import connexion
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app_connexion = connexion.FlaskApp("online-store", specification_dir="./")
app = app_connexion.app
app.config.from_object('project.config')
db = SQLAlchemy(app)
app_connexion.add_api("openapi.yml")


# Flow routes ----------------------------------------------------------------------------------------------------------
@app.before_request
def before_request():
    pass


@app.after_request
def after_request(response):
    return response


@app.teardown_request
def teardown_request(error):
    if error:
        print("closing request with server error...")


# Error routes ---------------------------------------------------------------------------------------------------------
@app.errorhandler(500)
def page_not_found(e):
    return jsonify({"Request Failed": [{"Status code": 500}, {'Details': f'{e}'}]})


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Request Failed": [{"Status code": 404}, {'Details': f'{e}'}]})


@app.errorhandler(409)
def page_not_found(e):
    return jsonify({"Request Failed": [{"Status code": 409}, {'Details': f'{e}'}]})
