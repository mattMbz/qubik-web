from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, InputRequired, Email, Length, Regexp


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
    submit = SubmitField('Register Now')
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


class CreateVirtualMachineForm(FlaskForm):
    virtual_machine_name = StringField('Virtual Machine Name (*)', validators=[InputRequired()])
    application_name = StringField('Application Name')
    version = StringField('Version')
    location_host = StringField('Location Host', render_kw={'disabled': True}, default='https://vmachines.unau.edu.ar')
    cpu = SelectField('V-CPU', choices=[('1 CPU', '1 CPU'), ('2 CPU', '2 CPU', ), ('4 CPU', '4 CPU')], default='1 CPU')
    ram = SelectField('V-RAM', choices=[('512MB', '512MB'), ('768MB', '768MB'), ('1GB', '1GB')], default='512MB')
    disk = SelectField('V-DISK', choices=[('4GB', '4GB'), ('10GB', '10GB'), ('80GB', '80GB')], default='4GB')
    submit = SubmitField('Create new VM')
#End_class

