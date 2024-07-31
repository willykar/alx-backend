#!/usr/bin/env python3
"""
4-app module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """didplays 4-index.html template """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """
    get_locale function
    Gets best match locale according to request"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
