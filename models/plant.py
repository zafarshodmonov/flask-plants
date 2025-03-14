from app import db

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_id = db.Column(db.Integer, db.ForeignKey('plant_names.id'), nullable=False)
    data = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Plant {self.name_id}>'
