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

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/month', methods=['GET'])
def evaluateMonth():
    selectedMonth = request.args.get('month-input')
    print(selectedMonth)
    data_ = model.get_evaluate_month(selectedMonth)
    return render_template('/index.html', data=data_, selectedMonth_=selectedMonth)

@app.route('/day', methods=['GET'])
def evaluateDay():
    selectedDay = request.args.get('day-input')
    print(selectedDay)
    data_ = model.get_evaluate_day(selectedDay)
    return render_template('/index.html', data=data_, selectedDay_=selectedDay)

@app.route('/week', methods=['GET'])
def evaluateWeek():
    selectedWeek = request.args.get('selected-week')
    print(selectedWeek)

@app.route('/evaluate', methods=['GET'])
def evaluate():
    selectedMonth = request.args.get('selected-month')
    selectedDay = request.args.get('selected-day')

    if selectedMonth:
        data = model.get_evaluate_month(selectedMonth)
        evaluation_counts = model.get_evaluate_month_count(selectedMonth)

    elif selectedDay:
        data = model.get_evaluate_day(selectedDay)
        evaluation_counts = model.get_evaluate_day_count(selectedDay)
    else:
        data = []

    return render_template('/index.html', data=data, _evaluation_counts=evaluation_counts)

@app.route('/index')
def evaluatee():
    data_ = model.get_evaluate()
    evaluation_counts = model.get_evaluate_count()
    return render_template('/index.html', data=data_, _evaluation_counts=evaluation_counts)


@app.route('/login', methods=['GET', 'POST'])
def loginn():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = authenticate_user(username, password)

        if user:
            # Establecer los datos de sesión para el usuario
            session['username'] = user['username']
            session['iduser'] = user['iduser']

            return redirect('/index')
        else:
            flash('Error, intentelo de nuevo', 'error')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['firstname']
        password = request.form['lastname']
        username = request.form['username']
        password = request.form['password']

        data = {
            'username': username,
            'password': password
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            host + '/user/add_user', json=data, headers=headers)

        return redirect('/index')

    return render_template('register.html')


@app.route('/logout')
def logout():
    # Eliminar la información de sesión del usuario
    session.pop('username', None)
    session.pop('role', None)

    # Redirigir al usuario a la página de inicio
    return render_template('home/index.html')

def execute_arduino_script():
    arduino_script_path = 'ArduinoPY.py'
    subprocess.Popen(['python', arduino_script_path])
def start_arduino_script():
    p = multiprocessing.Process(target=execute_arduino_script)
    p.start()

if __name__ == "__main__":      
    start_arduino_script()
    app.run(debug=True)