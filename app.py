from flask import Flask, request, jsonify, render_template, redirect, flash, session
from flask_session import Session
from flask_cors import CORS, cross_origin

import json
import requests
import subprocess
import multiprocessing



host = 'http://localhost:5000'
#################### MODELOS ########################
from controlers import ControllerHorary, ControllerLogin

LoginController = ControllerLogin.LoginController()
HoraryController = ControllerHorary.HoraryController()

################# CONTROLADORES #####################



################ CONFIGURACIONES ####################
app = Flask(__name__, template_folder='templates', static_folder='static')

cors = CORS(app)

app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'h2g3h32gh2'

Session(app)
#################### ERRORES ########################

# Manejador de error para el código de respuesta 403

#@app.errorhandler(403)
#def forbidden_error(error):
#    return render_template('home/page-403.html'), 403

# Manejador de error para el código de respuesta 404 Not Found

#@app.errorhandler(404)
#def not_found_error(error):
#    return render_template('home/page-404.html'), 404

# Manejador de error para el código de respuesta 500 Internal Server Error

#@app.errorhandler(500)
#def internal_error(error):
#    return render_template('home/page-500.html'), 500

###################### RUTAS ########################


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = LoginController.iniciate_session(username,password)

        if result == 1:
            # Establecer los datos de sesión para el usuario
            session['username'] = username
            return redirect('/interfazbase')
        
        elif result == 2:
            flash('Error, usuario no encontrado', 'error')
        else:
            flash('Error, contraseña incorrecta', 'error')

    return render_template('login.html')

@app.route('/interfazbase', methods=['GET', 'POST'])
def interfazbase():
    horary_result = HoraryController.horary_relationed(session['username'])
    return render_template('interfazbase.html', six_first_Horary = horary_result)

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
        create = LoginController.add_user(data)
        if(create):
            return redirect('/')
        else:
            flash('Error', 'error')

    return render_template('register.html')

@app.route('/logout')
def logout():
    # Eliminar la información de sesión del usuario
    session.pop('username', None)
    session.pop('role', None)

    # Redirigir al usuario a la página de inicio
    return render_template('presentacion.html')

@app.route('/buscarhorario', methods=['GET', 'POST'])
def buscarhorario():
    integrant = []
    title = ''
    autor = ''
    if(request.method == 'POST'):
        title = request.form['title']
        autor = request.form['autor']
        for i in range(3):
            if(request.form['email'+str(i)] != ''):
                integrant.append(request.form['email'+str(i)])

    horary_result = HoraryController.horary_filtrated(session['username'], title, autor, integrant)
    return render_template('buscarhorario.html', result_horary = horary_result, usuario = session['username'])

if __name__ == "__main__":      
    app.run(debug=True)