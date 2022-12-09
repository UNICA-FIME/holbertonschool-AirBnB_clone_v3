#!/usr/bin/python3
"""Script what run the app"""
from flask import Flask
from flask import make_response
from flask import jsonify
from models import storage
from api.v1.views import app_views
from flask import Blueprint
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """This is method call the method close"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Register a function to handle errors by code"""
    return (make_response(jsonify({"error": "Not found"}), 404))


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST'),
            port=int(getenv('HBNB_API_PORT')),
            threaded=True)
