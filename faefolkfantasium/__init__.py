import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the secret key for sessions and other secure features
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '7d81f958ff96f923e4329635a01f91ce48238be3260d1d7a')

# Check if running on Heroku (DATABASE_URL will be set on Heroku)
if 'DATABASE_URL' in os.environ:
    # Use the Heroku PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
else:
    # Use the absolute path to the local SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////workspace/faefolkfantasium/instance/beings.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")



