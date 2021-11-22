from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

import sqlalchemy
import logging

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

lgr = logging.getLogger(app.config['APP_NAME'])
lgr.setLevel(logging.DEBUG)
fh = logging.FileHandler(app.config['CSV_LOG_FILE'])
fh.setLevel(logging.DEBUG)

frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)

lgr.addHandler(fh)

from models import *
