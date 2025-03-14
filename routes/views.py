from flask import render_template, Blueprint
from models import Plant
from app import db

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    plants = Plant.query.all()
    return render_template("index.html", plants=plants)

@routes.route('/add_plant', methods=['POST'])
def add_plant():
    from flask import request, redirect, url_for
    from models.plant import Plant
    
    name_id = request.form.get('name_id')
    data = request.form.get('data')
    
    new_plant = Plant(name_id=name_id, data=data)
    from app import db
    db.session.add(new_plant)
    db.session.commit()
    
    return redirect(url_for('routes.get_plants'))
