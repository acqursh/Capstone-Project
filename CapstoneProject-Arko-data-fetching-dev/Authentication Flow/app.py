import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from Common.routes import initialize_routes
from Common.init_database import initialize_db, guard
from Common.logging import is_blacklisted
from Models.users import Users

load_dotenv()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:kunal1234@127.0.0.1:3306/capstone'
CLIENT_ID="238R4F"
CLIENT_SECRET="3a556b63e50ee80ad4469a1615e7b623"
SECRET_KEY="hi"

app = Flask(__name__)

CORS(app)
api = Api(app)

path = os.path.dirname(os.path.abspath(__file__))
upload_folder = os.path.join(
    path.replace("/file_folder", ""), "tmp")
os.makedirs(upload_folder, exist_ok=True)
#print(os.getenv('SQL_DATABASE_URI'))

app.config["UPLOAD_FOLDER"] = upload_folder
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY


guard.init_app(app, Users, is_blacklisted=is_blacklisted)
initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=7000,
        debug=True
    )
