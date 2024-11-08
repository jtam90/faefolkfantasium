from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/beings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")


db = SQLAlchemy(app)

from faefolkfantasium import routes


