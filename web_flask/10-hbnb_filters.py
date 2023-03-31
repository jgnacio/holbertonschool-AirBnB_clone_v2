#!/usr/bin/python3
"""
Created on Fri Mar 31 10:25:00 2023.

@authors: jgnacio
@description:
    This module provides a simple implementation of
    the web framework flask, and have this endpoints:

    (/hbnb_filters):
        Display the base web page of hbnb.

        Get the states and cities for the filter and order
        by the name with the jinja template.
"""
from flask import Flask
from flask import render_template
from models import State, Amenity
from models import storage

app = Flask(__name__)

storage.reload()


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Shutdown the current session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display the base web page of hbnb.

    Get the states and cities for the filter and order
    by the name.
    """
    states_sort = storage.all(State).values()
    amenities_sort = storage.all(Amenity).values()
    print(amenities_sort)
    return render_template(
        '10-hbnb_filters.html',
        states=states_sort,
        amenities=amenities_sort
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
