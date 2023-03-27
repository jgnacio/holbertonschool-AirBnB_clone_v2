#!/usr/bin/python3
"""
Created on Mon Mar 27 13:24:00 2023.

@authors: jgnacio
@description:
    This module is an update of 5-number_template.py that
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

    (/number/<int:n>):
        Display “n is a number” only if n is an integer.

    (/number_template/<int:n>):
        Display a HTML page only if n is an integer.
"""
from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page only if n is an integer.

    H1 tag: “Number: n is even|odd” inside the tag BODY.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
