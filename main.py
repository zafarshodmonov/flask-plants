from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class PlantName(db.Model):
    __tablename__ = 'plant_names'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latin = db.Column(db.String, nullable=False)
    
    translations = db.relationship('PlantNameTranslation', backref='plant_name', lazy=True)
    plants = db.relationship('Plant', backref='plant_name', lazy=True)

class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_id = db.Column(db.Integer, db.ForeignKey('plant_names.id'))
    data = db.Column(db.Text)

class PlantNameTranslation(db.Model):
    __tablename__ = 'plant_name_translations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant_names.id'))
    language = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_plant_name', methods=['POST'])
def add_plant_name():
    plant_name = request.form.get('name')

    if not plant_name:
        return "Error: Name field is required", 400

    new_plant = PlantName(latin=plant_name)
    db.session.add(new_plant)
    db.session.commit()

    return "Plant name added successfully!"

# Get all plant names
@app.route('/get_plant_names', methods=['GET'])
def get_plant_names():
    plant_names = PlantName.query.all()
    return jsonify([plant_name.latin for plant_name in plant_names])

# set plant 
@app.route('/set_plant', methods=['POST'])
def set_plant():
    plant_name = request.form.get('name')
    plant_data = request.form.get('data')

    if not plant_name or not plant_data:
        return "Error: Name and data fields are required", 400

    plant = PlantName.query.filter_by(latin=plant_name).first()
    if not plant:
        return "Error: Plant name not found", 404

    new_plant = Plant(name_id=plant.id, data=plant_data)
    db.session.add(new_plant)
    db.session.commit()

    return "Plant added successfully!"

# Get all plants
@app.route('/get_plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([{'name': plant.plant_name.latin, 'data': plant.data} for plant in plants])

if __name__ == '__main__':
    app.run(debug=True)
