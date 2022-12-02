"""
This script handles the login and logout functions.
It provides an access token which is used to access the restricted routes
"""
from flask import request, jsonify
from flask_restful import Resource

from Common.init_database import guard


class LoginAPI(Resource):

    def post(self):
        """
        Takes in registered email and password and returns an access token
        :return: JWT Token
        """
        json_data = request.get_json()
        username = json_data['email_id']
        password = json_data['password']

        user = guard.authenticate(username, password)
        token = guard.encode_jwt_token(user)
        return jsonify({'access_token': token})


blacklist = set()


def is_blacklisted(jti):
    return jti in blacklist


class LogoutAPI(Resource):

    def post(self):
        """
        Blacklists the token, so it cannot be used again and logs the user out
        """
        req = request.get_json(force=True)
        data = guard.extract_jwt_token(req['access_token'])
        blacklist.add(data['jti'])
        return jsonify(message='token blacklisted ({})'.format(req['access_token']))
