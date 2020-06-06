import os

from dotenv import load_dotenv

load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = True
    SQLALCHEMY_POOL_TIMEOUT = 3666
    SQLALCHEMY_POOL_RECYCLE = 3
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("TESTING_DATABASE_URL")
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig, testing=TestingConfig, prod=ProductionConfig
)

key = Config.SECRET_KEY
