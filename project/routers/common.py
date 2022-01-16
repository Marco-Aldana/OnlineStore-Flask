from flask import jsonify, request


# Basic routes ---------------------------------------------------------------------------------------------------------
def home():
    if request.method == 'GET':
        return jsonify({"description": "Hello world!! Im a get method"})
