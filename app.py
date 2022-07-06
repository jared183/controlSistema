from distutils import debug
from re import template
from xml.etree.ElementTree import QName
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

@app.route("/doc-venta")
def docVenta():
    return render_template('doc-venta.html')
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
    return render_template('general.html')

# ______________ Contratos en Proceso ______________

@app.route("/pendientes")
def pendientes():
    return render_template('pendiente.html')

@app.route("/finalizado")
def finalizado():
    return render_template('finalizados.html')

@app.route("/cancelados")
def cancelados():
    return render_template('cancelado.html')

# ______________ Facturación ______________

@app.route("/recibo")
def recibo():
    return render_template('recibo.html')

if __name__=='__main__':
    app.run(debug = True)