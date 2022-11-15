import datetime
from Common.init_database import db


class Fitbit_users(db.Model):
    email_id = db.Column(db.String(255), primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    access_token = db.Column(db.String(950))
    gender = db.Column(db.String(10))
    weight = db.Column(db.Float)
    age = db.Column(db.Integer)
    user_id = db.Column(db.String(45))
