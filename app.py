from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
from database import db

db.init_app(app)

# # Import routes after db initialization to prevent circular imports
# from routes import main as main_blueprint
# app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
