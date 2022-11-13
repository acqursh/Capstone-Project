import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from Common.routes import initialize_routes
from Common.init_database import initialize_db

load_dotenv()

app = Flask(__name__)

CORS(app)
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQL_DATABASE_URI')

initialize_db(app)
initialize_routes(api)

# db = SQLAlchemy(app)


# @app.route('/register')
# def register_user():  # put application's code here
#
#     main()
#     return 'Hello World!'
#
#
# @app.route('/attr')
# def get_user_attr():  # put application's code here
#
#     # main()
#     return 'Attr!'


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=7000,
        debug=True
    )
