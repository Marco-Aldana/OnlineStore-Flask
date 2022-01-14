from flask import Flask, jsonify

from configuration.database_connect import database_connection_alchemy, init_database

app = Flask(__name__)

with app.app_context():  # To set tables in database
    database_connection_alchemy()
    init_database()

@app.route("/")
def index():
    return jsonify({"message": "Hello world!!"})

@app.before_first_request
def initialize():
    pass

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'errorCode': 404, 'message': 'Route not found'})


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
