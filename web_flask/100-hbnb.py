#!/usr/bin/python3
""" a script to start a flask app """
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def dispose(exception):
    """ Exit the session of sql """
    storage.close()


@app.route('/hbnb')
def hbnb_filters():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    data = {
        'states': list(states.values()),
        'amenities': list(amenities.values()),
        'places': list(places.values())
    }
    return render_template('100-hbnb.html', **data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
