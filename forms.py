from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='El username es requerido'), 
        Length(max=10, message='El username debe tener como máximo 10 caracteres'),
        Length(min=4, message="El username debe tener como mínimo 4 caracteres")
    ])
    email = StringField('Email', validators=[
        DataRequired(message='El email es requerido'), 
        Email(message='El email no es válido')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='La contraseña es requerida'), 
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres'),
        Regexp(r'.*[A-Z].*', message='La contraseña debe contener al menos una letra mayúscula')
    ])
    submit = SubmitField('Registrarse')
#End_class


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='The email is required.'),
        Email(message='El email no es válido')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='The password is required.')
    ])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')
#End_class