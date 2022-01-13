from flask import Flask, current_app, flash, jsonify, make_response, redirect, request, url_for
from werkzeug import Response
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!!"


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'errorCode': 404, 'message': 'Route not found'})


if __name__ == '__main__':
    app.debug = True
    app.run()
