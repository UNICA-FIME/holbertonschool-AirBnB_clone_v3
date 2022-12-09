#!/usr/bin/python3
""" Script return json"""
from api.v1.views import app_views
from flask import jsonify


dict_json = {"status": "OK"}


@app_views.route('/status', strict_slashes=False)
def status():
    return (jsonify(dict_json))
