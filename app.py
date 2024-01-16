from flask import Flask, request, jsonify, render_template, redirect, flash, session
from flask_session import Session
from flask_mail import Mail, Message
from flask_cors import CORS, cross_origin

import json
import requests
import subprocess
import multiprocessing

from models.ModelUser import UserModel



host = 'http://localhost:5000'
#################### MODELOS ########################
from controlers import ControllerHorary, ControllerLogin, ControllerIntegrant

LoginController = ControllerLogin.LoginController()
HoraryController = ControllerHorary.HoraryController()
IntegrantController = ControllerIntegrant.IntegrantController()
ModelUser = UserModel()

##################### CONTROLADORES #####################



#################### CONFIGURACIONES ####################

app = Flask(__name__, template_folder='templates', static_folder='static')

cors = CORS(app)

app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'h2g3h32gh2'
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'schedulewiseoficial@gmail.com'
app.config['MAIL_PASSWORD'] = 'clrdydazxjyeciex'

mail = Mail(app)
Session(app)

####################### RUTAS #######################

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
    username_ = session['username']
    userData = ModelUser.get_user_username(username_)
    print(userData)
    horary_result = HoraryController.horary_relationed(username_)
    return render_template('interfazbase.html', six_first_Horary = horary_result, userData = userData)

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
    return render_template('index.html')

@app.route('/crearhorario', methods=['POST'])
def crearhorario():
    title = request.form['title']
    description = request.form['description']
    HoraryController.create_horary(session['username'], title, description)
        
    return redirect('/buscarhorario')

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


@app.route('/horario/<string:id>', methods=['GET'])
def get_hours_by_horary_id_route(id: str):
    horarios = HoraryController.get_hours_by_horary_id_controller(id)[0]
    return render_template('horario.html', data = horarios, identificador = id)

@app.route('/horario/<string:id>/integrantes', methods=['GET'])
def verintegrantes(id: str):
    integrantes = HoraryController.get_integrants(id)
    return render_template('integrantes.html', integrantes = integrantes, identificador = id, autoria = HoraryController.check_autor(id, session['username']))

@app.route('/horario/<string:id>/integrantes/aceptar', methods=['GET'])
def aceptarinvitacion(id):
    if(session.get('username')):
        IntegrantController.add_integrant(session['username'],str(id))
        return redirect('/buscarhorario')
    else:
        return redirect('/login')

@app.route('/horario/<string:id>/integrantes/invitar', methods=['POST'])
def enviarinvitacion(id):
    email = request.form['email_integrante']
    data = {
        'app_name': "ScheduleWise",
        'title' : "Invitación de parte de " + str(session['username']),
        'body' : "Te han invitado para que participes en el horario",
    }
    sender = "noreply@app.com"
    msg = Message(data['title'], sender=sender, recipients=[email])
    msg.html = render_template("sendemail.html", data=data, id=id)

    try:
        mail.send(msg)
        print ("La invitación fue enviado de forma correcta")
        return redirect('/horario/'+str(id)+'/integrantes')
    except Exception as e:
        print(f"La invitación no fue enviado de forma correcta, tal vez el correo no exista {e}")
        return redirect('/horario/'+str(id)+'/integrantes')

if __name__ == "__main__":      
    app.run(debug=True)