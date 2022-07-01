from distutils import debug
from re import template
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/inicio")
def inicio():
    return render_template('index.html')

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/password")
def contraseña():
    return render_template('password.html')

@app.route("/register")
def registrar():
    return render_template('register.html')

@app.route("/404")
def error404():
    return render_template('404.html')

if __name__=='__main__':
    app.run(debug = True)