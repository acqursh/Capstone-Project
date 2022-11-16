from Resources.user_attr import FitbitUserAttrSchema
from Common.init_database import db
from Common.api_response import ApiResponse
from Models.user_attr import User_attr

from flask_restful import Resource
from flask import make_response

schema = FitbitUserAttrSchema(many=True)
api_response = ApiResponse()


class GetUsers(Resource):
    def get(self):
        try:
            users = User_attr.query.all()
            for user in users:
                print(user.email, user.sex)
            return schema.dump(User_attr.query.all())

        except Exception as e:
            db.session.rollback()
            error = e
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = "Please enter valid data"
            api_response.status = "Fail"

            return make_response(api_response.to_json(), 500)
