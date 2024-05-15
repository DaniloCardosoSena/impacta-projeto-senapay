from datetime import datetime
import random
import string
from decimal import Decimal
from sqlalchemy import Column, DECIMAL
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    saldo = db.Column(DECIMAL(precision=10, scale=2), nullable=False)
    conta = db.Column(db.String(20), nullable=False, unique=True)
    agencia = db.Column(db.String(20), nullable=False, unique=True)

    def check_password(self, password):
        return self.password == password

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.generate_random_values()

    def generate_random_values(self):
        self.saldo = round(random.uniform(50, 1000), 2)
        self.conta = self.generate_random_conta()
        self.agencia = self.generate_random_agencia()

    @staticmethod
    def generate_unique_conta():
        while True:
            conta = generate_random_conta()
            existing_user = User.query.filter_by(conta=conta).first()
            if not existing_user:
                return conta

    @staticmethod
    def generate_random_conta():
        prefixo = random.randint(1000, 9999)
        sufixo = random.randint(1, 9)
        return f"{prefixo}-{sufixo}"

    def generate_random_agencia(self):
        return ''.join(random.choices(string.digits, k=3))

class Transfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    sender_account = db.Column(db.String(20), nullable=False)
    receiver_account = db.Column(db.String(20), nullable=False)
    agencia_receiver = db.Column(db.String(20), nullable=False)
    agencia_sender = db.Column(db.String(20), nullable=False)