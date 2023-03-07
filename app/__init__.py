from flask import Flask
from config import Config

# Flask-SQLAlchemy and Flask-Migrate initialization
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

# db info
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# add models (classes) for db 
from app import routes, models