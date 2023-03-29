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
from flask import Flask
from flask import render_template
from models import State
from models import storage

app = Flask(__name__)

storage.reload()


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Shutdown the current session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display all states with the id and sorted by the name."""
    new_dict = dict(sorted(storage.all(State).items(),
                    key=lambda item: item[1].name))
    return render_template('7-states_list.html', states=new_dict.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
