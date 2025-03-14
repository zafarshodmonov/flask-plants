from flask import Blueprint, jsonify, request
from models.plant import Plant
from models.database import db

plant_routes = Blueprint('plant_routes', __name__)

@plant_routes.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return {"plants": [plant.name for plant in plants]}
