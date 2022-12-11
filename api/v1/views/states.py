#!/usr/bin/python3
""" new view for State objects that handles all default RESTFul API actions"""
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort
from flask import make_response
from flask import request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states_get():
    """Retrieves the list of all State objects"""
    dict_new = storage.all(State).values()
    list_states = []
    for item in dict_new:
        list_states.append(item.to_dict())
    return (jsonify(list_states))


@app_views.route('/states/<path:state_id>', methods=['GET'], strict_slashes=False)
def states_get_id(state_id):
    """Retrieves the list of all State objects"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return (jsonify(state.to_dict()))


@app_views.route('/states/<path:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def states_delete(state_id):
    """Deletes a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return (make_response(jsonify({}), 200))


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def states_post():
    """Creates a State"""
    if not request.get_json():
        return abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        return abort(400, description="Missing name")

    new_data = request.get_json()
    new_state = State(**new_data)
    new_state.save()
    return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<path:state_id>', methods=['PUT'], strict_slashes=False)
def states_put(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    list_key = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in list_key:
            setattr(State, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
