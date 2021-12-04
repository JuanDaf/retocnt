
from flask import Flask, render_template, request, redirect, url_for
from flask.wrappers import Request
from flask_mysqldb import MySQL

app =  Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reto'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pacientes')
def pacientes():
    return render_template('pacientes.html')

@app.route('/addpacientes',methods=['POST'])
def addpacientes():
    if request.method == 'POST':
        documento = request.form['documento']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        edad = request.form['edad']
        direccion = request.form['direccion']
        sexo = request.form.get('sexo')
        fumador = request.form.get('fumador1')
        fumadorr = request.form['fumador']
        estatura = request.form['estatura']
        peso = request.form['peso']
        dieta = request.form.get('dieta')

        if fumador == "1":
            fumador = fumadorr +' años' 
            con = mysql.connection.cursor()
            con.execute('INSERT INTO pacientes VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (documento,nombres,apellidos,edad,direccion,sexo,peso,estatura,fumador,dieta,12,'ok','ok',4))
            mysql.connection.commit()
        else :
            fumador = 'no'
            con = mysql.connection.cursor()
            con.execute('INSERT INTO pacientes VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (documento,nombres,apellidos,edad,direccion,sexo,peso,estatura,fumador,dieta,12,'ok','ok',4))
            mysql.connection.commit()
        print(documento, nombres, apellidos, edad, direccion, sexo, peso, estatura, fumador, dieta)
    return 'bien'

@app.route('/verpacientes')
def ver():
    return 'verpacientes'


@app.route('/editar')
def editar():
    return 'editar'

if __name__ == '__main__':
    app.run(port = 3300, debug= True)
