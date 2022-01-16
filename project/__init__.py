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
    print("starting request--------------------------------------------------")


@app.after_request
def after_request(response):
    print("finalizing request--------------------------------------------------")
    return response


@app.teardown_request
def teardown_request(error):
    print("teardown request--------------------------------------------------")
    if error:
        print("closing request with server error...")


# Error routes ---------------------------------------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'errorCode': 404, 'message': 'Route not found'})


@app.errorhandler(500)
def page_not_found(e):
    return jsonify({'errorCode': 500, 'message': 'Internal server error'})
