#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)  # instance of Flask class


@app.route('/', strict_slashes=False)  # decorator
# fuction that returns Hello HBNB!
def hello_hbnb():
    """ Function that returns Hello HBNB! """
    return 'Hello HBNB!'  # return Hello HBNB!


@app.route('/hbnb', strict_slashes=False)  # decorator
def hbnb():
    """ Function that returns HBNB! """
    return 'HBNB'  # return HBNB!


@app.route('/c/<text>', strict_slashes=False)  # decorator
def c_text(text):
    """ Function that returns C followed by text """
    text = text.replace('_', ' ')  # replace _ with space
    return 'C {}'.format(text)  # return C followed by text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # run app on port 5000
