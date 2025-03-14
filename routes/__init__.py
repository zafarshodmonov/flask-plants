from flask import Blueprint
from .plant_routes import plant_routes

def register_blueprints(app):
    app.register_blueprint(plant_routes, url_prefix="/plants")
