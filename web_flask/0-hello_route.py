#!/usr/bin/python3
"""
a script that starts a Flask web application
Requirements:
web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
must use the option strict_slashes=False in your route definition
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


if __name__ == '__main__':
    app.run()
