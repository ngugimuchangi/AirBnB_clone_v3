#!/usr/bin/python3
""" Endpoints for place related
    interactions
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/cities/<city_id>/places', strict_slashes=False,
                 methods=['GET', 'POST'])
def place_by_city(city_id):
    """search for a city with given id and:
       return all list of its places
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if request.method == 'GET':
        return jsonify([place.to_dict() for place in city.places])

    if request.method == 'POST':
        data = get_json(request)
        if not data:
            return make_response('Not a JSON\n', 400)
        if 'user_id' not in data.keys():
            return make_response('Missing user_id\n', 400)
        if 'name' not in data.keys():
            return make_response('Missing name\n', 400)
        if storage.get(User, data.get('user_id')) is None:
            abort(404)
        data.update({'city_id': city_id})
        new_place = Place(**data)
        new_place.save()
        return make_response(jsonify(new_place.to_dict()), 201)


@app_views.route('/places/<place_id>', strict_slashes=False,
                 methods=['GET', 'PUT', 'DELETE'])
def place_by_id(place_id):
    """search for a place with given id and:
        1. return it
        2. update it
        3. delete it
       depending on the method
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(place.to_dict())

    if request.method == 'DELETE':
        storage.delete(place)
        storage.save()
        return make_response(jsonify({}), 200)

    if request.method == 'PUT':
        data = get_json(request)
        if not data:
            return make_response('Not a JSON\n', 400)
        for key, value in data.items():
            if key not in ['id', 'user_id', 'created_at', 'updated_at']:
                setattr(place, key, value)
        place.save()
        return make_response(jsonify(place.to_dict()), 200)


def get_json(request):
    """check if body has json data
       and handles errors reponses
    """
    #  exception handling to avoid calling
    #  on_json_loading_failed()
    try:
        data = request.get_json()
    except Exception:
        data = None
    return data
