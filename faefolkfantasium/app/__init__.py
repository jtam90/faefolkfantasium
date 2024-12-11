import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Load environment variables from .env file if it exists
load_dotenv()

# Initialize the database and migration instances globally (but don't bind them yet)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Set the secret key for sessions and other secure features
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')  # Add a fallback default value

    # Get the DATABASE_URL from environment variables
    database_url = os.getenv('DATABASE_URL')
    
    # Check if DATABASE_URL is present
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set. Please configure it in your .env file.")
    
    # Fix Heroku's database URL format if necessary
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    
    # Set the SQLALCHEMY_DATABASE_URI configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

    # Disable Flask-SQLAlchemy event system to save memory and avoid warnings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Set upload folder and allowed file extensions
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'static/uploads')  # Default to 'static/uploads'
    app.config['ALLOWED_EXTENSIONS'] = set(os.getenv('ALLOWED_EXTENSIONS', 'png,jpg,jpeg,gif').split(','))  # Default extensions

    # Initialize the database and migration with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Print the configured database URI (optional, for debugging)
    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # Import and register routes
    from . import routes  # Ensure that routes.py uses `app.route` directly

    return app
