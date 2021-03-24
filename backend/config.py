import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = False
# Enable debug mode.
DEBUG = True

# Connect to the database
DB_HOST = os.getenv('DB_HOST', 'localhost:5432')  
DB_USER = os.getenv('DB_USER', 'postgres')  
DB_PASSWORD = os.getenv('DB_PASSWORD', '0000')  
DB_NAME = os.getenv('DB_NAME', 'trivia')  
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False

