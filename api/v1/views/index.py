#!/usr/bin/python3
""" views functionality
"""
from api.v1.views import app_views
<<<<<<< HEAD
from flask import jsonify
from models import storage
=======
from flask import jsonify, make_response
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
>>>>>>> f893bb456cc14a164d157732f9faebe1052b4baa


@app_views.route('/status', methods=['GET'])
def status():
    """ return status OK on route /status"""
<<<<<<< HEAD
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
=======
    return make_response(jsonify({"status": "OK"}))


@app_views.route('/stats', methods=['GET'])
def stats():
    """ returns count of all objects per class"""
    classes = {"amenities": Amenity, "cities": City, "places": Place,
               "reviews": Review, "states": State, "users": User}

    obj_count = {key: storage.count(value) for key, value in classes.items()}
    return make_response(jsonify(obj_count))
>>>>>>> f893bb456cc14a164d157732f9faebe1052b4baa
