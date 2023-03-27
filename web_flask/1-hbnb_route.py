#!/usr/bin/python3
"""
Created on Mon Mar 27 10:41:00 2023.

@authors: jgnacio
@description:
    This module provides a simple web application
    with the flask framework, and have this endpoints
    available:

    (/):
        Root of the application that have a function
        called say_hello() that return the simple
        string "Hello HBNB!".
    (/hbnb):
        have a function called hbnb() that return
        the simple string "HBNB".
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """Return hello HBNB on /."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB on /hbnb end point."""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
