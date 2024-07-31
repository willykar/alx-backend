#!/usr/bin/env python3
""" 2-app module """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """Defines app route /"""
    return render_template('2-index.html')


class Config:
    """Config class to setup Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the language to use"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
