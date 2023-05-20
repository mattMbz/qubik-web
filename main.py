import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, current_user, login_user, logout_user

from werkzeug.urls import url_parse
from dotenv import load_dotenv

from forms import SignupForm, SignInForm
from models import User, users, get_user


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap = Bootstrap5(app)
login_manager = LoginManager(app)
login_manager.login_view = "show_signin_form"

virtual_machines = ['nodejs-app', 'Debian10-vm', 'flaskapi', 'vm-universidad']

vms = {
    'virtual_machines' : virtual_machines,
    'numbers' : len(virtual_machines)
}


@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template("index.html", **vms)
    else:
        return redirect(url_for('welcome'))
#End_def


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
#End_def

@app.route('/delete')
def delete():
    return render_template('/admin/delete_vm.html')
#End_def

@app.route('/monitor')
def monitor():
    return render_template('/admin/monitor.html')
#End_def

@app.route('/tasks')
def tasks():
    return render_template('/admin/tasks.html')
#End_def

@app.route('/createvm')
def create_vm():
    return render_template('/admin/create_vm.html')
#End_def

@app.route("/vmachine/<string:slug>")
def show_virtual_machine(slug):
    return render_template('vm_view.html', slug_title=slug)
#End_def


@app.route("/admin/vmachine") # Route for create new VM
@app.route("/admin/vmachine/<int:vm_id>") # Route for update an exists Vm
def create_virtual_machine(vm_id=None):
    return render_template("admin/vm_form.html", vm_id=vm_id)
#End_def


@app.route("/signup", methods=["GET", "POST"])
def show_signup_form():
    form = SignupForm()
    if form.validate_on_submit():  # Realizar validación del formulario
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, username, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    else:
        flash_errors(form)  # Mostrar mensajes de error
        
    return render_template("signup.html", form=form)
#End_def


@app.route("/signin", methods=["GET", "POST"])
def show_signin_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = SignInForm()

    context = {
        'form': form,
    }

    if form.validate_on_submit():
        user = get_user(form.email.data)
        
        if user is not None and user.check_password(form.password.data):
            print(f"user:{user.email}, password: {form.password.data}")
            print("User has been signin")
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')

            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            
            return redirect(next_page)
        else:
            if (user is None):
                error='The user does not exist, please signup first.'
                context['error'] = error
            else:
                if user.check_password(form.password.data) == False:
                    error='Incorrect password!'
                    context['error'] = error
            
    else:
        flash_errors(form)
    
    return render_template("login.html", **context)
#End_def


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{field}: {error}", "error")
# End_def


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None
#End_def


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
#End_def
