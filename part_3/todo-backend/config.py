import os
basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

class Config(object):
    DEBUG = False
    TESTING = False
    APP_SETTINGS = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/postgres'
    FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', '5000')

# Production config variables
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
