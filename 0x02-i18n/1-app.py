#!/usr/bin/env python3
""" 1-app module """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """Define an app route /"""
    return render_template('1-index.html')


class Config:
    """ Config class that setups up Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


if __name__ == '__main__':
    app.config.from_object(Config)
    app.run(debug=True)
