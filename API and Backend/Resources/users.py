from Common.init_database import db
from Common.api_response import ApiResponse
from Models.fitbit_users import Fitbit_users
from Resources.register_fitbit import FitbitUserSchema

from flask_restful import Resource
from flask import make_response


schema = FitbitUserSchema(many=True)
api_response = ApiResponse()


class User(Resource):
    def get(self):
        try:
            users = Fitbit_users.query.all()
            for user in users:
                print(user.email_id, user.gender)
            return schema.dump(Fitbit_users.query.all())

        except Exception as e:
            db.session.rollback()
            error = e
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = "Please enter valid data"
            api_response.status = "Fail"

            return make_response(api_response.to_json(), 500)




