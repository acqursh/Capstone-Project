from Resources.users import RegisterUser
from Resources.user_attr import GetUserAttr


def initialize_routes(api):
    api.add_resource(RegisterUser, "/register/<string:email>")
    api.add_resource(GetUserAttr, "/users/<string:email_id>")
