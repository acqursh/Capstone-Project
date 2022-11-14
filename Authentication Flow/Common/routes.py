from Resources.register_users import RegisterUser
from Resources.user_attr import GetUserAttr
from Resources.ecg_reader import ReadECG


def initialize_routes(api):
    api.add_resource(RegisterUser, "/register/<string:email>")

    api.add_resource(GetUserAttr, "/users/<string:email_id>")

    api.add_resource(ReadECG, "/ecg/<string:email_id>")
