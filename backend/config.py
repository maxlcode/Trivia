import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = False
# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:0000@localhost:5432/trivia'
SQLALCHEMY_TRACK_MODIFICATIONS = False

