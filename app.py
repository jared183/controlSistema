from distutils import debug
from re import template
from flask import Flask, render_template, url_for

app = Flask(__name__)

# ______________ Rutas Principales ______________

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/inicio")
def inicio():
    return render_template('index.html')



# ______________ Generar Contrato plan venta______________

@app.route("/venta")
def planVenta():
    return render_template('plan-venta.html')

# ______________ Generar Contrato plan renta ______________


@app.route("/renta")
def planRenta():
    return render_template('plan-renta.html')

@app.route("/doc-renta")
def docRenta():
    return render_template('doc-renta.html')

# ______________ Contratos Generales ______________

@app.route("/general")
def contratoGeneral():
    return render_template('contrato.html')

# ______________ Contratos en Proceso ______________

@app.route("/pendientes")
def pendientes():
    return render_template('')

@app.route("/finalizado")
def finalizado():
    return render_template('')

@app.route("/cancelados")
def cancelados():
    return render_template('')

# ______________ Facturación ______________

@app.route("/recibo")
def recibo():
    return render_template('')

if __name__=='__main__':
    app.run(debug = True)