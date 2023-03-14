#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask 
app = Flask(__name__)  # instance of Flask class

route = app.route('/', strict_slashes=False)  # decorator
@route # decorator
# function that returns Hello HBNB!
def hello_hbnb():
    """ Function that returns Hello HBNB! """
    return 'Hello HBNB!'  # return Hello HBNB!
# should listen  on port 5000 and route /hbnb


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # run app on port 5000
