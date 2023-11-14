from flask import Flask, render_template, session, request, redirect, url_for,flash
app = Flask(__name__)
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

app.secret_key='mysecretkey'

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(port=3000,debug=True)