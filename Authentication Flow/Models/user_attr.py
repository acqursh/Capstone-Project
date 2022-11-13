from Common.init_database import db


class User_attr(db.Model):
    email = db.Column(db.String(255), primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    cp = db.Column(db.Integer)
    trtbps = db.Column(db.Integer)
    chol = db.Column(db.Integer)
    fbs = db.Column(db.Integer)
    restecg = db.Column(db.Integer)
    thalachh = db.Column(db.Integer)
    slp = db.Column(db.Integer)
    target = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
