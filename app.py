from flask import Flask, render_template, session, request, redirect, url_for,flash
import mariadb
from controladores import ControladorLogin
app = Flask(__name__)
conn = mariadb.connect(
         host='127.0.0.1',
         port=3306,
         user='root',
         password='kerito17',
         database='organizadorhorarios')

cur = conn.cursor()

@app.route('/')
def home():
    ControladorLogin.comprobar_login(cur,'ugafuwh@gmail.com','12345678')
    return render_template('index.html')

if __name__=='__main__':
    app.run(port=3000,debug=True)