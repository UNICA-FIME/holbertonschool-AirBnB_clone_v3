#!/usr/bin/python3
"""Script what run the app"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST'),
            port=int(getenv('HBNB_API_PORT')),
            threaded=True)
