from flask import jsonify, request

from project import app


# Basic routes ---------------------------------------------------------------------------------------------------------
@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        return jsonify({"description": "Hello world!! Im a get method"})


# Flow routes ----------------------------------------------------------------------------------------------------------
"""
@app.before_request
def before_request():
    pass

@app.after_request
def after_request():
    print("after request")

@app.teardown_request
def teardown_request():
    print("teardown request")
"""


# Error routes ---------------------------------------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'errorCode': 404, 'message': 'Route not found'})
