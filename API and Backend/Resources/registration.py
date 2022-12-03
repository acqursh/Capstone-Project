import re

from flask import request, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError, DataError

from Common.api_response import ApiResponse
from Common.init_database import db, guard
from Models.users import Users
api_response = ApiResponse()


class Registration(Resource):

    def post(self):
        """Posts a users and account to the common while registration.

        :return:
        :raises: IntegrityError: If account_name and email already exist in the common.
                 KeyError: If any fields of the JSON data are left empty
        """
        try:
            data = request.json
            post1 = Users(
                email_id=data['email_id'],
                password=guard.hash_password(data['password'])
            )
            db.session.add(post1)
            db.session.commit()
            api_response.status = "Success"
            api_response.message = "User registered"
            api_response.success.clear()
            api_response.errors.clear()
            api_response.success.append('Data added to the database')

        except KeyError as e:
            db.session.rollback()
            error = "Column " + str(e) + " is empty"
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = "Please fill all the columns"
            api_response.status = "Fail"
            return make_response(api_response.to_json(), 500)

        except IntegrityError as e:
            db.session.rollback()
            error = "Account already exists"
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = "Please enter valid data"
            api_response.status = "Fail"
            return make_response(api_response.to_json(), 500)

        except Exception as e:
            db.session.rollback()
            string = e.args[0]
            result = re.findall(r'\(.*?\)', string)
            if len(result) != 0:
                errors = result[1].strip("()")
                error = errors.split(",")
                error = str(error[1])
                error = error.strip("\" \"")
            else:
                error = str(e)
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = "Please enter valid data"
            api_response.status = "Fail"

            return make_response(api_response.to_json(), 500)

        return make_response(api_response.to_json(), 200)
