# __init__.py or app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the database and migration extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Application Factory for creating the Flask app."""
    app = Flask(__name__)

    # Set secret key
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

    # Configure SQLAlchemy database URI
    database_url = os.getenv('DATABASE_URL', 'sqlite:///local.db')
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    # Disable SQLAlchemy track modifications to save resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import routes and models inside the factory function to avoid circular imports
    from .models import Being
    from .routes import bp  # Assuming you have a 'bp' blueprint in routes.py
    app.register_blueprint(bp)

    return app

