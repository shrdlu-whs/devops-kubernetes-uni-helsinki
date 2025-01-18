import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    APP_SETTINGS = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT',5000)
    FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST',"127.0.0.1")
    TODO_BACKEND_HOST = os.getenv('TODO_BACKEND_HOST',"http://todo-backend-svc")
    TODO_BACKEND_PORT = os.getenv('TODO_BACKEND_PORT',5000)
    TODO_BACKEND_URL = f'{TODO_BACKEND_HOST}:{TODO_BACKEND_PORT}'

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
