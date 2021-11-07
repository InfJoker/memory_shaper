import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class Prod(Config):
    DEBUG = False


class Dev(Config):
    DEVELOPMENT = True


class Test(Config):
    TESTING = True
