from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

import sqlalchemy

app = Flask(__name__)


def get_config_object_name(env_name):
    return 'config.' + env_name


def get_db():
    return db


def new_sql_session() -> sqlalchemy.orm.Session:
    return Session()


app.config.from_object(get_config_object_name(os.environ['APP_ENVIRONMENT']))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Session = sessionmaker(bind=db.engine)

from models import *
