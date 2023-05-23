#!/usr/bin/env python3

"""
A flask application
"""
from flask_babel import Babel
from flask import Flask
from flask import render_template


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the applicatioN
app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    render an html template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
