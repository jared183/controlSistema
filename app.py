from distutils import debug
from re import template
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug = True)