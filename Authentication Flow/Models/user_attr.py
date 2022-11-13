import datetime
from Common.init_database import db


class User_attr(db.Model):
    # __tablename__ = 'user_attr'
    email = db.Column(db.String(255))
    user_id = db.Column(db.String(45), primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    cp = db.Column(db.Integer)
    trestbps = db.Column(db.Integer)
    chol = db.Column(db.Integer)
    fbs = db.Column(db.Integer)
    restecg = db.Column(db.Integer)
    thalach = db.Column(db.Integer)
    exang = db.Column(db.Integer)
    oldpeak = db.Column(db.Float)
    slope = db.Column(db.Integer)
    ca = db.Column(db.Integer)
    thal = db.Column(db.Integer)
    target = db.Column(db.Integer)
