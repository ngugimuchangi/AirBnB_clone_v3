#!/usr/bin/python3
""" views functionality
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ return status OK on route /status"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'])
def obj_stats():
    """return count of objects by type in JSON format"""
    objects = {}
    a_dict = {
        'Amenity':  'amenities',
        'City':  'cities',
        'Place':  'places',
        'Review':  'reviews',
        'User':  'users',
        'State':  'states'
    }
    for key, val in a_dict.items():
        objects[val] = storage.count(key)
    return jsonify(objects)
