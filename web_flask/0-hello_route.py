#!/usr/bin/python3
"""
a script that starts a Flask web application
Requirements:
web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
must use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    Route:
    /: displays “Hello HBNB!”
    """
    return (f"Hello HBNB!")


if __name__ == "__main__":
    app.run()
