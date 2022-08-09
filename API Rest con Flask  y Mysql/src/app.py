from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from validaciones import *
from config import config

app = Flask(__name__)

# CORS(app)
CORS(app, resources={r"/cursos/*": {"origins": "http://localhost"}})

conexion = MySQL(app)

# @cross_origin
@app.route('/cursos',methods=['GET'])
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Codigo, Nombre, Creditos FROM curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos=[]
        for fila in datos:
            curso = {'codigo':fila[0], 'nombre':fila[1],"credito":fila[2]}
            cursos.append(curso)
        return jsonify({'cursos':cursos,'mensaje':"Cursos listados.",'exito':True})
    except Exception as ex:
        return jsonify({'message' : "Error", 'exito': False})


def leer_curso_db(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Codigo, Nombre, Creditos FROM curso WHERE codigo =  '{0}'".format(codigo)
        cursor.execute(sql)
        datos= cursor.fetchone()
        if datos != None:
            curso = {'codigo':datos[0], 'nombre':datos[1],"credito":datos[2]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/cursos/<string:codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        curso = leer_curso_db(codigo)
        if curso != None:
            return jsonify({'curso':curso,'mensaje': "Curso encontrado", 'exito':True})
        else:
            return jsonify({'mensaje':"Curso no encontrado",'exito':False})
    except Exception as ex:
        return jsonify({'message' : "Error", 'exito':False})

@app.route('/cursos', methods=['POST'])
def add_curso():
    # print(request.json)
    if (validar_codigo(request.json['Codigo']) and validar_nombre(request.json['Nombre'])
        and validar_creditos(request.json['Creditos'])):

        try:
            curso = leer_curso_db(request.json['Codigo'])
            if curso != None:
                return jsonify({'message':"Codigo ya existe, no se puede duplicar", 'exito':False})
            else:
                cursor = conexion.connection.cursor()
                sql = """INSERT INTO curso (Codigo, Nombre, Creditos) 
                    VALUES ('{0}', '{1}', {2})""".format(request.json['Codigo'],
                    request.json['Nombre'], request.json['Creditos'])
                cursor.execute(sql)
                conexion.connection.commit() # Esto confirma la accion que estamos
                return jsonify({'message' : "Curso registrado",'exito': True})
        except Exception as ex:
            return jsonify({'message' : "Error", 'exito': False})
    else:
        return jsonify({'message': "Parametros invalidos...",'exito':False})

@app.route('/cursos/<string:codigo>',methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        curso = leer_curso_db(codigo)
        if curso !=None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM curso WHERE codigo =  '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit() # Esto confirma la accion que estamos
            return jsonify({'message' : "Curso eliminado",'exito':True})
        else:
            return jsonify({'message' : "Curso no encontrado",'exito':False})
    except Exception as ex:
        return jsonify({'nessage' : "Error", 'exito': False})


@app.route('/cursos/<string:codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    if (validar_codigo(codigo) and validar_nombre(request.json['Nombre'])
        and validar_creditos(request.json['Creditos'])):

        try:
            curso = leer_curso_db(codigo)
            if curso != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE curso SET Nombre = '{0}', Creditos = {1} 
                WHERE Codigo = '{2}' """.format(request.json['Nombre'], request.json['Creditos'],codigo)
                cursor.execute(sql)
                conexion.connection.commit() # Esto confirma la accion que estamos
                return jsonify({'message' : "Curso actualizado", 'exito': True})
            else:
                return jsonify({'message' : "Curso no encontrado", 'exito': False})
        except Exception as ex:
            return jsonify({'message' : "Error",'exito': False})
    else:
        return jsonify({'message': "Parametros invalidos...",'exito':False})


def pagina_no_encontrada(error):
    return "<h1>La pagina que intenta buscar no existe</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()