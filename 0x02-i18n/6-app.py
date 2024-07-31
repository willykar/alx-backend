#!/usr/bin/env python3
"""
5-app module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Class Config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """
    index function
    renders 6-index.html
    """
    return render_template("6-index.html")


@babel.localeselector
def get_locale():
    """Gets best fmatch locale according to request"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    get_user function that
    returns a given user"""
    user_id = request.args.get('login_as')

    if user_id is None:
        return None

    return users.get(int(user_id))


@app.before_request
def before_request():
    """
    before_request method
    sets a user object to flask.g"""
    user = get_user()
    g.user = user


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
