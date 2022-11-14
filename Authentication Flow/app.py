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

path = os.path.dirname(os.path.abspath(__file__))
upload_folder = os.path.join(
    path.replace("/file_folder", ""), "tmp")
os.makedirs(upload_folder, exist_ok=True)

app.config["UPLOAD_FOLDER"] = upload_folder
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQL_DATABASE_URI')

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=7000,
        debug=True
    )
