from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


def get_config_object_name(env_name):
    return 'config.' + env_name


def get_db():
    return db


app.config.from_object(get_config_object_name(os.environ['APP_ENVIRONMENT']))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *
