#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)  # decorator
@app.route('/python/<text>', strict_slashes=False)  # decorator
def python(text='is cool'):
    """ Function that returns Python is cool! """
    # text = request.args.get('text', default='is cool')  # get text from url
    text = text.replace('_', ' ')  # replace _ with space
    return 'Python {}'.format(text)  # return Python followed by text


@app.route('/number/<int:n>', strict_slashes=False)  # decorator
def number(n):
    """ Function that returns n is a number! """
    # check is n is a number and return n is a number
    # if type(n) == int: or below:
    if isinstance(n, int):
        return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)  # decorator
#display html body only if n is an integer
def number_template(n):
    """ Function that returns n is a number! """
    # check is n is a number and return n is a number
    # if type(n) == int: or below:
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # run app on port 5000
