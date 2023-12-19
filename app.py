from flask import Flask, request, jsonify, render_template, redirect, flash, session
from flask_session import Session
from flask_cors import CORS, cross_origin

import json
import requests
import subprocess
import multiprocessing

from models.model import TaskModel

host = 'http://localhost:5000'

model = TaskModel()

app = Flask(__name__, template_folder='templates', static_folder='static')

cors = CORS(app)

app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'h2g3h32gh2'

Session(app)
#################### ERRORES ########################

# Manejador de error para el código de respuesta 403

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('home/page-403.html'), 403

# Manejador de error para el código de respuesta 404 Not Found

@app.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404

# Manejador de error para el código de respuesta 500 Internal Server Error

@app.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500

##################### FUNCIONES ######################

def authenticate_user(username, password):

    user = model.get_user_username(username)
    if user and user['password'] == password:
        return user
    return None

###################### RUTAS ########################


@app.route('/index')
def index():
    return render_template('/index.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = authenticate_user(username, password)

        if user:
            # Establecer los datos de sesión para el usuario
            session['email'] = user['email']

            return redirect('/index')
        else:
            flash('Error, intentelo de nuevo', 'error')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        data = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'password': password
        }
        create = model.add_user(data)
        if(create):
            return redirect('/login')
        else:
            flash('Error', 'error')

    return render_template('register.html')

@app.route('/logout')
def logout():
    # Eliminar la información de sesión del usuario
    session.pop('username', None)
    session.pop('role', None)

    # Redirigir al usuario a la página de inicio
    return render_template('index.html')


if __name__ == "__main__":      
    app.run(debug=True)