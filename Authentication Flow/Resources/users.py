import base64
import json
import os
import sys
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask_restful import Resource
import tempfile
from sqlalchemy.exc import IntegrityError
from flask import request, make_response

from dotenv import load_dotenv

import jwt
import keyboard
import requests
import sqlalchemy as db
from Common.init_database import db
from Models.users import Users
from Common.api_response import ApiResponse

load_dotenv()
api_response = ApiResponse()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')


class RegisterUser(Resource):

    @staticmethod
    def make_request():
        url = f"https://www.fitbit.com/oauth2/authorize?response_type=code&client_id={client_id}&" \
              "redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Flogin&scope=activity%20heartrate" \
              "%20location%20nutrition%20profile%20settings%20sleep%20social%20weight%20" \
              "oxygen_saturation%20respiratory_rate%20temperature&expires_in=604800"

        webbrowser.open(url, new=1, autoraise=True)

    @staticmethod
    def wait_for_response(temp_file, server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
        server_address = ('', 8080)
        httpd = server_class(server_address, handler_class)
        buffer = 1
        sys.stderr = open(temp_file.name, 'w', buffer)
        return httpd.handle_request()

    @staticmethod
    def read_log(temp_file):
        try:
            with open(temp_file.name, "r") as file:
                for line in file:
                    pass
                last_line = line
            return last_line[54:-16]

        except Exception as e:
            print(e)

    @staticmethod
    def close_tab():
        keyboard.press_and_release('ctrl+w')

    @staticmethod
    def get_token(temp_file, token_file):
        try:
            token = f"{client_id}:{client_secret}"
            auth_token = str(base64.b64encode(token.encode("ascii")))
            headers = {
                'Authorization': f'Basic {auth_token[2:-1]}',
            }
            code = RegisterUser.read_log(temp_file)

            data = {
                'clientId': f'{client_id}',
                'grant_type': 'authorization_code',
                'redirect_uri': 'http://localhost:8080/login',
                'code': f'{code[:-1]}',
            }

            response = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=data)
            token = json.loads(response.text)
            encrypted_token = {}
            for i in token:
                try:
                    encrypted_token[i] = token[i]
                except Exception as e:
                    print(e)
            encoded = jwt.encode(encrypted_token, 'secret', algorithm='HS256')

            with open(token_file.name, "w") as file:
                file.write(encoded)

        except Exception as e:
            print(e)

    @staticmethod
    def restore_token(refresh_token):
        token = f"{client_id}:{client_secret}"
        auth_token = str(base64.b64encode(token.encode("ascii")))
        headers = {
            'accept': 'application/json',
            'authorization': f'Basic {auth_token[2:-1]}',
            'content-type': 'application/x-www-form-urlencoded',
        }

        data = f'grant_type=refresh_token&refresh_token={refresh_token}'

        response = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=data)

        token = json.dumps(response.json(), indent=4)

        with open("token.json", "w") as file:
            file.write(token)

    @staticmethod
    def get_user(access_token):
        headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {access_token}',
        }

        response = requests.get('https://api.fitbit.com/1/user/-/profile.json', headers=headers)
        user_info = response.json()
        details = {}
        lst = ["age", "firstName", "lastName", "gender", "weight", "encodedId"]
        for i in user_info['user']:
            if i in lst:
                details[i] = user_info['user'][i]

        return details

    @staticmethod
    def add_user(Details, Access_token):
        # try:
        # encoded = jwt.encode(Access_token, 'secret', algorithm='HS256')
        user = Users(
            access_token=Access_token,
            age=Details['age'],
            first_name=Details['firstName'],
            last_name=Details['lastName'],
            user_id=Details['encodedId'],
            gender=Details['gender'],
            weight=Details['weight']
        )
        db.session.add(user)
        db.session.commit()

    # except Exception as e:
    #     print("Nor in main")
    #     db.session.rollback()
    #     print(e)
    # print("user already exists")

    def get(self):
        try:
            temp = tempfile.NamedTemporaryFile(delete=False)
            token = tempfile.NamedTemporaryFile(delete=False)
            RegisterUser.make_request()
            RegisterUser.wait_for_response(temp)
            RegisterUser.close_tab()
            time.sleep(2)
            RegisterUser.get_token(temp, token)
            temp.flush()
            temp.close()
            with open(token.name, "r") as f:
                encoded = f.read()

            decoded = jwt.decode(encoded, 'secret', algorithms=['HS256'])
            user_details = RegisterUser.get_user(decoded['access_token'])
            RegisterUser.add_user(user_details, encoded)
            # restore_token(json_obj['refresh_token'])
            token.flush()
            token.close()

            api_response.success.clear()
            api_response.errors.clear()
            api_response.message = "User resource added to the database"
            api_response.status = "Success"
            api_response.success.append('Data added to the database')
            return make_response(api_response.to_json(), 200)

        except IntegrityError as e:
            db.session.rollback()
            error = "The given account is mapped to other resources," \
                    " please delete them first"
            api_response.success.clear()
            api_response.errors.clear()
            api_response.errors.append(error)
            api_response.message = "Please delete mapped resources first"
            api_response.status = "Fail"
            return make_response(api_response.to_json(), 500)

        except Exception as e:
            db.session.rollback()
            print(e)
            time.sleep(10)
