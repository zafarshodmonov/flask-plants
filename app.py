from flask import Flask
from models.database import db
from routes import register_blueprints
from config import Config

config_object = Config()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config_object.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config_object.SQLALCHEMY_TRACK_MODIFICATIONS

# Ma'lumotlar bazasini boshlash
db.init_app(app)

# Blueprint'larni registratsiya qilish
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
