#!/usr/bin/python3
""" a script to start a flask app """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ a function that display  Hello Hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ a function that display hbnb """
    return 'HBNB'


@app.route('/c/<text>')
def c_compliment(text):
    """a function that says C and a msg """
    message = text.replace('_', ' ')
    return 'C %s' % message


@app.route('/python/')
@app.route('/python/<text>')
def python_compliment(text='is_cool'):
    """ fct that display a msg after a python msg """
    message = text.replace('_', ' ')
    return 'Python %s' % message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
