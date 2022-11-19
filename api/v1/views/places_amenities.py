#!/usr/bin/python3
""" Endpoints for place_amenity related
    interactions
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route('/places/<place_id>/amenities', strict_slashes=False,
                 methods=['GET'])
def place_amenities(place_id):
    """search for a place with given id and:
       return a list of its amenities
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify([amenity.to_dict() for amenity in place.amenities])


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 strict_slashes=False,
                 methods=['DELETE', 'POST'])
def update_place_amenities(place_id, amenity_id):
    """search for a place and amenity with given ids and:
        1. remove/unlink amenity from the place
        2. add/link amenity to the place
       depending on the method
    """
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None:
        abort(404)

    if request.method == 'DELETE':
        if amenity in place.amenities:
            place.amenities.pop(place.amenities.index(amenity))
            place.save()
        else:
            abort(404)
        return make_response(jsonify({}), 200)

    if request.method == 'POST':
        if amenity in place.amenities:
            return make_response(jsonify(amenity.to_dict()), 200)
        place.amenities.append(amenity)
        place.save()
        return make_response(jsonify(amenity.to_dict()), 201)
