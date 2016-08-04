from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#Create an Instance of Flask
app = Flask(__name__)

#Include config from config.py
app.config.from_object('config')

#Create an instance of SQLAclhemy
db = SQLAlchemy(app)

from app import views, models