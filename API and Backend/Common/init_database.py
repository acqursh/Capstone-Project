from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_praetorian import Praetorian

db = SQLAlchemy()
ma = Marshmallow()
api = Api()
guard = Praetorian()


def initialize_db(app):
    db.init_app(app)
