from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Ensure 'app' is properly defined

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import routes (relative import)
from . import routes


