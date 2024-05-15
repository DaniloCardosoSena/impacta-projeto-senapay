from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User, Transfer

class RegistrationForm(FlaskForm):
    username = StringField('Nome Completo', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirme a Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

class TransferForm(FlaskForm):
    conta = StringField('Conta', validators=[DataRequired()])
    agencia = StringField('Agência', validators=[DataRequired()])
    valor = FloatField('Valor', validators=[DataRequired()])
    receiver_account = StringField('Conta do Recebedor', validators=[DataRequired()])
    agencia_receiver = StringField('Agência do Recebedor', validators=[DataRequired()])
    submit = SubmitField('Transferir')

    def validate_conta(self, conta):
        user = User.query.filter_by(conta=conta.data).first()
        if not user:
            raise ValidationError('Conta não encontrada.')

    def validate_agencia(self, agencia):
        user = User.query.filter_by(agencia=agencia.data).first()
        if not user:
            raise ValidationError('Agência não encontrada.')

    def validate_receiver_account(self, receiver_account):
        user = User.query.filter_by(conta=receiver_account.data).first()
        if not user:
            raise ValidationError('Conta do beneficiário não encontrada.')

    def validate_agencia_receiver(self, agencia_receiver):
        user = User.query.filter_by(agencia=agencia_receiver.data).first()
        if not user:
            raise ValidationError('Agência do beneficiário não encontrada.')