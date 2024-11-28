import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Initialize the database and migration instances globally (but don't bind them yet)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Set the secret key for sessions and other secure features
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Check if running on Heroku (DATABASE_URL will be set on Heroku)
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        # Fix Heroku's database URL format if necessary
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # Use the absolute path to the local SQLite database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////workspace/faefolkfantasium/instance/beings.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Now initialize the database and migration with the app
    db.init_app(app)
    migrate.init_app(app, db)

    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # Import and register routes here if needed
    # from . import routes
    # app.register_blueprint(routes.bp)

    return app
