from Resources.users import RegisterUser


def initialize_routes(api):
    api.add_resource(RegisterUser, "/register")
