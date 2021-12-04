
from os import walk
from flask import Flask, render_template, request, redirect, url_for, flash
from flask.wrappers import Request
from flask_mysqldb import MySQL

app =  Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reto'
mysql = MySQL(app)


app.secret_key = 'secreto'

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

        
        if direccion == "" or  sexo ==""  or dieta =="" or documento == "" or nombres == "" or apellidos == "" or edad == "" or peso == ""  or estatura == ""  or fumador == "":
            flash('Campos vacios, Corrobora Información')
            return redirect(url_for('pacientes'))

        else:
            print('Paso por Aca')
            if fumadorr == "":
               fumadorr = int(fumador)
        
            fumadorr =  int(fumadorr)
       
             #Peso estatura, esto en funcion de la div de peso entre estatura, obteniedo un punto flotante que se valiad de 0 a 1. Por ende se toma referncia de 0 a 1  
            pesoestatura = (int(peso) / int(estatura))
            if  pesoestatura <= (0.25):
                pesoestatura = 1
            elif pesoestatura >= (0.26) and pesoestatura <=(0.50):
                pesoestatura = 2
            elif pesoestatura >= (0.51) and pesoestatura <=(0.75):
                pesoestatura = 3;
            else:
                pesoestatura = 4
        
            #Seccion de calcuala la prioridad para el paciente 
            prioridad = 0;

            edad =  int(edad)
            if edad >= 1 and edad <=15:
                if edad >= 1 and edad <= 5:
                    prioridad = (pesoestatura + 3)
                elif edad >= 6 and edad <= 12:
                    prioridad = (pesoestatura + 2)
                elif edad >=13 and edad <=15:
                    prioridad = (pesoestatura + 1)

            elif edad >= 16 and edad <= 40:
                if fumadorr > 1:
                    prioridad = ((fumadorr /4)+ 2)
                else:
                    prioridad = 2
            elif edad > 41:
                if dieta == "Si":
                    if edad >=60 and edad <= 100:
                        prioridad = ((edad/20)+4)
                else:
                    prioridad = ((edad /30) +3)
        
            #Seccion de calcular el riesgo 
            if edad >=1 and edad <=40:
                riesgo  = ((edad * prioridad)/100)
            else:
                riesgo =  (((edad *prioridad)/100) +5.3)




            if fumadorr == "":
                fumadorr = int(fumador)
        
                fumadorr =  int(fumadorr)
       
                #Peso estatura, esto en funcion de la div de peso entre estatura, obteniedo un punto flotante que se valiad de 0 a 1. Por ende se toma referncia de 0 a 1  
            pesoestatura = (int(peso) / int(estatura))
            if  pesoestatura <= (0.25):
                pesoestatura = 1
            elif pesoestatura >= (0.26) and pesoestatura <=(0.50):
                pesoestatura = 2
            elif pesoestatura >= (0.51) and pesoestatura <=(0.75):
                pesoestatura = 3;
            else:
                pesoestatura = 4
        
            #Seccion de calcuala la prioridad para el paciente 
            prioridad = 0;

            edad =  int(edad)
            if edad >= 1 and edad <=15:
                if edad >= 1 and edad <= 5:
                    prioridad = (pesoestatura + 3)
                elif edad >= 6 and edad <= 12:
                    prioridad = (pesoestatura + 2)
                elif edad >=13 and edad <=15:
                    prioridad = (pesoestatura + 1)

                elif edad >= 16 and edad <= 40:
                    if fumadorr > 1:
                        prioridad = ((fumadorr /4)+ 2)
                    else:
                        prioridad = 2
                elif edad > 41:
                    if dieta == "Si":
                        if edad >=60 and edad <= 100:
                            prioridad = ((edad/20)+4)
                    else:
                        prioridad = ((edad /30) +3)
        
            #Seccion de calcular el riesgo 
            if edad >=1 and edad <=40:
                riesgo  = ((edad * prioridad)/100)
            else:
                riesgo =  (((edad *prioridad)/100) +5.3)
                fumador = int(fumador)
        if fumador == 0:
            fumador = fumadorr  
            estatura = estatura + ' Cm'
            con = mysql.connection.cursor()
            con.execute('INSERT INTO pacientes VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (documento,nombres,apellidos,edad,direccion,sexo,peso,estatura,fumador,dieta,pesoestatura,'Pendiente',prioridad,riesgo))
            mysql.connection.commit()
        else :
            fumador = "No"
            con = mysql.connection.cursor()
            con.execute('INSERT INTO pacientes VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (documento,nombres,apellidos,edad,direccion,sexo,peso,estatura,fumador,dieta,pesoestatura,'Pendiente',prioridad,riesgo))
            mysql.connection.commit()
    flash('Registro almacenado')
    return redirect(url_for('pacientes'))
    
    
    
@app.route('/verpacientes')
def ver():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM pacientes Where Estado = "Pendiente" ORDER by Riesgo DESC' )
    data = con.fetchall()
    print(data)
    return render_template('pacientesr.html', datos = data)

@app.route('/verpacientesp')
def verr():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM pacientes Where Estado = "Pendiente" ORDER by Prioridad DESC' )
    data = con.fetchall()
    print(data)
    return render_template('pacientesp.html', datos = data)

@app.route('/atender/<Documento>')
def atender(Documento):
    con = mysql.connection.cursor()
    con.execute('UPDATE pacientes SET Estado = %s WHERE Documento = %s ', ('Atendido',Documento))
    mysql.connection.commit()
    flash('Paciente atendido')
    return redirect(url_for('ver'))

@app.route('/atenderr/<Documento>')
def atenderr(Documento):
    con = mysql.connection.cursor()
    con.execute('UPDATE pacientes SET Estado = %s WHERE Documento = %s ', ('Atendido',Documento))
    mysql.connection.commit()
    flash('Paciente atendido')
    return redirect(url_for('verr')) 

@app.route('/indicadores')
def indicador():
    con = mysql.connection.cursor()
    con.execute('SELECT Documento, Nombres, Apellidos, Edad, Estado  FROM pacientes Where Fumador > 1 and Estado = "Pendiente" ORDER by Prioridad' )
    data = con.fetchall()
    print(data)
    con = mysql.connection.cursor()
    con.execute('SELECT Nombres,Apellidos,MIN(Edad)as Edad, Estado  FROM pacientes Where  Estado = "Pendiente" ' )
    data2 = con.fetchall()
    print(data2)
    con = mysql.connection.cursor()
    con.execute('SELECT Nombres,Apellidos,MAX(Edad)as Edad, Estado  FROM pacientes Where  Estado = "Pendiente" ' )
    data3 = con.fetchall()
    print(data3)
    return render_template('indicadores.html', datos= data, datos2 = data2, datos3 = data3)

if __name__ == '__main__':
    app.run(port = 3300, debug= True)
