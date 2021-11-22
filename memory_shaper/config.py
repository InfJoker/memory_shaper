import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    CSV_LOG_FILE = 'log/memory_shaper.csv'
    APP_NAME = 'memory_shaper'


class Prod(Config):
    DEBUG = False


class Dev(Config):
    DEVELOPMENT = True


class Test(Config):
    TESTING = True
