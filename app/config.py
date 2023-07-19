# Define the application directory
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Load environment variables
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Config(object):
    # Signal application everytime there is a change in Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    THREADS_PER_PAGE = 2
    SECRET_KEY = os.environ["SECRET_KEY"]
    UPLOAD_EXTENSIONS = [".xlsx", ".xls"]


class DevelopmentConfig(Config):
    # Statement for enabling the development environment
    ENV = "development"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
