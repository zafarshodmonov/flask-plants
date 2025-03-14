from flask import Blueprint, request, jsonify
from app import db
from models.plant import Plant

plant_routes = Blueprint('plant_routes', __name__)

@plant_routes.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return {"plants": [{"id": p.id, "name_id": p.name_id, "data": p.data} for p in plants]}

@plant_routes.route('/plants', methods=['POST'])
def add_plant():
    from flask import request
    data = request.json
    new_plant = Plant(name_id=data['name_id'], data=data.get('data', ''))
    db.session.add(new_plant)
    db.session.commit()
    return {"message": "Plant added successfully"}

#app.register_blueprint(plant_routes)
