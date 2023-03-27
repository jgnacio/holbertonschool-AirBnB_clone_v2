#!/usr/bin/python3
"""
Created on Mon Mar 27 11:13:00 2023.

@authors: jgnacio
@description:
    This module is an update of 2-c_route.py that
    provides a simple web application with the flask
    framework, and have this endpoints available:

    (/):
        Root of the application that have a function
        called say_hello() that return the simple
        string "Hello HBNB!".

    (/hbnb):
        have a function called hbnb() that return
        the simple string "HBNB".

    (/c/<text>):
        Display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space ).

    (/python):
        Display “Python is cool”.

    (/python/<text>):
        Display “Python ” followed by the value of the text variable.
        (replace underscore _ symbols with a space ).

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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Display “C ” followed by the value of the text variable.

    (replace underscore _ symbols with a space ).
    """
    return f'C_{text}'.replace("_", " ")


@app.route('/python', defaults={'text': "is_cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Display “Python ” followed by the value of the text variable.

    (replace underscore _ symbols with a space ).
    """
    return f'Python_{text}'.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
