
import os
from dotenv import load_dotenv

load_dotenv()

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False


class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# class TestingConfig(Config):
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.getenv("DB_TEST_URI")
#     PRESERVE_CONTEXT_ON_EXCEPTION = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = True


# class ProductionConfig(Config):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.getenv("DB_PROD_URI")


config_by_name = dict(
    dev=DevelopmentConfig,
    # test=TestingConfig,
    # prod=ProductionConfig
)

key = Config.SECRET_KEY