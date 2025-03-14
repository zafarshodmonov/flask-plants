from app import db

class PlantNames(db.Model):
    __tablename__ = 'plant_names'

    id = db.Column(db.Integer, primary_key=True)
    latin = db.Column(db.String(255), nullable=False)
    russian = db.Column(db.String(255), nullable=True)
    uzbek = db.Column(db.String(255), nullable=True)

    plants = db.relationship('Plant', backref='plant_name', lazy=True)

    def __repr__(self):
        return f'<PlantNames {self.id} - Latin: {self.latin}>'
    