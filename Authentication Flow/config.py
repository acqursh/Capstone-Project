import os
import dotenv

dotenv.load_dotenv()

class Config:
    """
    Project level config class
    """
    # pylint: disable=too-few-public-methods
    # Key Config
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')