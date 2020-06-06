from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    """Create app with given config.

    Parameters
    ----------
    config_name : str
        It can be dev or prod depending of which kind of env you want to use.

    Returns
    -------
    app
        flask app instance with related db.
    """
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    return app
