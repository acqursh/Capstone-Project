from Common.init_database import ma, db, guard
from Common.api_response import ApiResponse
from Models.accounts import Accounts

from flask_restful import Resource
from flask import make_response, request

import jwt
from sqlalchemy.exc import IntegrityError


class LoginSchema(ma.Schema):
    class Meta:
        fields = (
            'email_id', 'password', 'name'
        )


schema = LoginSchema()
api_response = ApiResponse()


class LoginUser(Resource):
    def post(self):
        try:
            details = request.json
            print(details)
            account = Accounts(
                email_id=details["email_id"],
                password=details["password"],
                name=details["name"]
            )

            db.session.add(account)
            db.session.commit()
            api_response.success.clear()
            api_response.errors.clear()
            api_response.message = "Account added to the database"
            api_response.status = "Success"
            api_response.success.append('Data added to the database')

            return make_response(api_response.to_json(), 200)

        except IntegrityError as e:
            db.session.rollback()
            error = "Account already exists"
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = "Please enter valid data"
            api_response.status = "Fail"

            return make_response(api_response.to_json(), 500)




