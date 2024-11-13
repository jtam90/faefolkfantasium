from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/workspace/faefolkfantasium/faefolkfantasium/static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


app.config['SECRET_KEY'] = '6f07d007de9eaa171ac81830ea8235'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////workspace/faefolkfantasium/instance/beings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")


db = SQLAlchemy(app)

from faefolkfantasium import routes


