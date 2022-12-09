#!/usr/bin/python3
""" Script return json"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


dict_json = {"status": "OK"}

"""classes = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
        }
"""

@app_views.route('/status', strict_slashes=False)
def status():
    return (jsonify(dict_json))


@app_views.route('/stats', strict_slashes=False)
def stats_objtects():
    """return amount of objet for class"""
    obj_res = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    
    return jsonify(obj_res)
