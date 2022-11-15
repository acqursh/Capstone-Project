import sqlalchemy
from Models.user_attr import User_attr
from Models.fitbit_users import Fitbit_users
from Common.init_database import ma, db
from Common.api_response import ApiResponse

from flask_restful import Resource
from flask_praetorian import auth_required, current_user
from flask import make_response, request

import requests
import jwt
from sqlalchemy.exc import IntegrityError


class FitbitUserAttrSchema(ma.Schema):
    class Meta:
        fields = (
            'email', 'user_id', 'age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'slp', 'output'
        )


schema = FitbitUserAttrSchema()
api_response = ApiResponse()


class GetUserAttr(Resource):
    @auth_required
    def post(self):
        try:
            json_data = request.json
            user = Fitbit_users.query.filter_by(email_id=current_user().email_id).first()
            decoded = jwt.decode(user.access_token, 'secret', algorithms=['HS256'])
            access_token = decoded['access_token']
            headers = {
                'accept': 'application/json',
                'authorization': f'Bearer {access_token}',
            }
            url = f"https://api.fitbit.com/1/user/{user.user_id}/activities/heart/date/2022-11-09/1d.json"
            response = requests.get(url, headers=headers, timeout=5)
            data = response.json()['activities-heart']
            response.close()
            ZoneList = data[0]
            thalach = []
            heartRateZones = ZoneList['value']

            for heart_rate in heartRateZones['heartRateZones']:
                if heart_rate['caloriesOut'] > 0:
                    if heart_rate['name'] == 'Peak':
                        maxHR = heart_rate['max'] - user.age
                        # print(heart_rate, maxHR)
                        thalach.append((maxHR + heart_rate['min']) / 2)
                    else:
                        print(heart_rate, (heart_rate['max'] + heart_rate['min']) // 2)
                        thalach.append((heart_rate['max'] + heart_rate['min']) // 2)

            if user.gender == "MALE":
                gender = 1

            else:
                gender = 0

            try:
                user_attr = User_attr(
                    email=current_user().email_id,
                    age=user.age,
                    sex=gender,
                    thalachh=max(thalach),
                    cp=json_data['cp'],
                    trtbps=json_data['trtbps'],
                    chol=json_data['chol'],
                    fbs=json_data['fbs'],
                    slp=json_data['slp']
                )
                db.session.add(user_attr)
                db.session.commit()

                api_response.success.clear()
                api_response.errors.clear()
                api_response.message = "User attributes added to the database"
                api_response.status = "Success"
                api_response.success.append('Data added to the database')
                return make_response(api_response.to_json(), 200)

            except sqlalchemy.exc.IntegrityError as e:
                db.session.rollback()
                user_attr = User_attr.query.get_or_404(current_user().email_id)

                if 'cp' in request.json:
                    user_attr.cp = request.json['cp']

                if 'trtbps' in request.json:
                    user_attr.trtbps = request.json['trtbps']

                if 'chol' in request.json:
                    user_attr.password = request.json['chol']

                if 'fbs' in request.json:
                    user_attr.fbs = request.json['fbs']

                if 'slp' in request.json:
                    user_attr.slp = request.json['slp']

                user_attr.thalachh = max(thalach)

                db.session.commit()

                api_response.success.clear()
                api_response.errors.clear()
                api_response.message = "User resource modified in the database"
                api_response.status = "Success"
                api_response.success.append('Data appended in the database')

                return make_response(api_response.to_json(), 200)

        except Exception as e:
            db.session.rollback()
            error = "Something went wrong please check the data again"
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = e
            api_response.status = "Fail"
            return make_response(api_response.to_json(), 500)
