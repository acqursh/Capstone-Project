import datetime
from Common.init_database import db


class Users(db.Model):
    # __tablename__ = 'users'
    user_id = db.Column(db.String(45), primary_key=True)
    email = db.Column(db.String(255))
    # password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    access_token = db.Column(db.String(950))
    gender = db.Column(db.String(10))
    weight = db.Column(db.Float)
    age = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
