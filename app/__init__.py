""""
Main application directory module
"""
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

sqlalchemy = SQLAlchemy()
migrate = Migrate()


config = Config()
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


def create_app(config_obj=None) -> Flask:
    """
    Creates and configures the Flask application.

    Args:
        config_obj: An optional configuration object to load configuration from.
        If None, the default configuration is used.

    Returns:
        The configured Flask application.
    """
    app = Flask(__name__)
    if config_obj is None:
        app.config.from_object(config)
    else:
        app.config.from_object(config_obj)
    initialize_extentions(app)
    register_blueprints(app)

    with app.app_context():
        sqlalchemy.create_all()
    return app


def initialize_extentions(app):
    """
    Initializes extensions used by the Flask application.

    Args:
        app: The Flask application instance.

    """
    sqlalchemy.init_app(app)
    migrate.init_app(app, sqlalchemy)
    CORS(app, resources={r"/api/*": {"origins": "*"}})


def register_blueprints(app):
    """
    Registers blueprints with the Flask application.

    Args:
        app: The Flask application instance.
    """
    from app.api import api

    app.register_blueprint(api)
