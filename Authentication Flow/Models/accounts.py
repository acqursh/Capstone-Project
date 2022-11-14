from Common.init_database import db


class Accounts(db.Model):
    email_id = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255))
