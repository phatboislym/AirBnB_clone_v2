#!/usr/bin/python3
"""
a script that starts a Flask web application
Requirements:
web application must be listening on 0.0.0.0, port 5000
Routes:
/: displays “Hello HBNB!”
/hbnb: displays “HBNB”
/c/<text>: displays “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space)
must use the option strict_slashes=False in your route definition
/python/(<text>): display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
"""
from flask import Flask as flask

app = flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route:
    /: displays 'Hello HBNB!'
    """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route:
    /hbnb: displays “HBNB”
    """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """
    Route:
    /c/<text>: displays “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    response = "C {}".format(text)
    return (response)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text="is cool"):
    """
    Route:
    /python/(<text>): display “Python ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
    """
    text = text.replace("_", " ")
    response = "Python {}".format(text)
    return (response)


if __name__ == '__main__':
    app.run()
