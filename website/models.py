from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(30))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())