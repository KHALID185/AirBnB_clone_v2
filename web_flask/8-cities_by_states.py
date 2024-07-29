#!/usr/bin/python3
""" a script to start a flask app """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def dispose(exception):
    """ a fct to remove the session """
    storage.close()


@app.route('/cities_by_states')
def states():
    """ fct that show all state """
    states = storage.all(State)
    states_list = list(states.values())
    return render_template('8-cities_by_states.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
