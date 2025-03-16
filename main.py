from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class PlantName(db.Model):
    __tablename__ = 'plant_names'
    id = db.Column(db.BigInteger, primary_key=True)
    latin = db.Column(db.String, nullable=False)
    
    translations = db.relationship('PlantNameTranslation', backref='plant_name', lazy=True)
    plants = db.relationship('Plant', backref='plant_name', lazy=True)

class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.BigInteger, primary_key=True)
    name_id = db.Column(db.BigInteger, db.ForeignKey('plant_names.id'))
    data = db.Column(db.Text)

class PlantNameTranslation(db.Model):
    __tablename__ = 'plant_name_translations'
    id = db.Column(db.BigInteger, primary_key=True)
    plant_id = db.Column(db.BigInteger, db.ForeignKey('plant_names.id'))
    language = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()

# Foydalanuvchi qo'shish
@app.route('/add_plant_name/<name>')
def add_plant_name(name):
    plant_name = PlantName(latin=name)
    db.session.add(plant_name)
    db.session.commit()
    return "Plant name added!"

if __name__ == '__main__':
    app.run(debug=True)
