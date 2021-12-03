from flask import Flask, render_template
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

@app.route('/verpacientes')
def ver():
    return 'verpacientes'


@app.route('/editar')
def editar():
    return 'editar'

if __name__ == '__main__':
    app.run(port = 3300, debug= True)
