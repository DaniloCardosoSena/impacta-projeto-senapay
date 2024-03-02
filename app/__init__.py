from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

class Config:
    # Configurações gerais do Flask
    SECRET_KEY = 'admin123'

    # Configurações do banco de dados PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://adminpay:admin@localhost/senapay'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes