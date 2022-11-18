#!/usr/bin/python3
""" Flask api to resturn status
"""
from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """ destroys DB session in case of DB storage
        reloads objects in case of File Storage
    """
    storage.close()


if __name__ == "__main__":
    #  get host address
    host = getenv('HBNB_API_HOST')
    if host is None:
        host = '0.0.0.0'

    #  get port number
    port = getenv('HBNB_API_PORT')
    if port is None:
        port = '5000'

    app.run(host=host, port=port)
