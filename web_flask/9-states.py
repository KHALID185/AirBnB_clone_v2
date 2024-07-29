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


@app.route('/states/')
@app.route('/states/<id>')
def states_and_state(id=None):
    """ fct that show all state """
    if id:
        id = 'State.{}'.format(id)
    return render_template('9-states.html', states=storage.all(State), id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
