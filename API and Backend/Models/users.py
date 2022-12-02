from Common.init_database import db


class Users(db.Model):
    email_id = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255))

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, email_id):
        return cls.query.filter_by(email_id=email_id).one_or_none()

    @classmethod
    def identify(cls, email_id):
        return cls.query.get(email_id)

    @property
    def identity(self):
        return self.email_id
