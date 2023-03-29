#!/usr/bin/python3
"""
Created on Wed Mar 29 10:23:00 2023.

@authors: jgnacio
@description:
    This module provides a simple implementation of
    the web framework flask, and have this endpoints.

    (/states_list):
        Display all states with the id and sorted by
        the name.
"""
from os import getenv
from flask import Flask
from flask import render_template
from models import State, City
from models import storage
from sqlalchemy.inspection import inspect

app = Flask(__name__)

storage.reload()


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Shutdown the current session."""
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    """Display all states with the id and sorted by the name."""
    new_dict = dict(sorted(storage.all(State).items(),
                    key=lambda item: item[1].name))
    return render_template('8-cities_by_states.html', states=new_dict.values())


@app.route('/states/<id>', strict_slashes=False)
def list_states_by_id(id):
    """List all states by given id and their associated cities."""
    new_dict = dict(sorted(storage.all(State).items(),
                    key=lambda item: item[1].name))
    for state in new_dict.values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return "<h1>Not found!<h1/>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
