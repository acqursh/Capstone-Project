from Resources.register_fitbit import RegisterFitbit
from Resources.user_attr import UserAttrs
from Resources.ecg_reader import ReadECG
from Resources.users import User
from Common.logging import LoginAPI, LogoutAPI
from Resources.registration import Registration
from Resources.get_user import GetUsers


def initialize_routes(api):
    api.add_resource(LoginAPI, "/login")

    api.add_resource(LogoutAPI, "/logout")

    api.add_resource(Registration, "/register")

    api.add_resource(RegisterFitbit, "/fitbit_register")

    api.add_resource(UserAttrs, "/user_attr")

    api.add_resource(User, "/users")

    api.add_resource(GetUsers, "/users_attr")

    api.add_resource(ReadECG, "/ecg")
