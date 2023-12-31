from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.estudiantes_model import EstudianteModel
model = EstudianteModel()


estudiante_blueprint = Blueprint('estudiante_blueprint', __name__)


@estudiante_blueprint.route('/create_estudiante', methods=['PUT'])
@cross_origin()
def create_estudiante(): #Crear un nuevo estudiante
    content = model.create_estudiante(request.json['dni'], request.json['nombres'], request.json['apellidos'],request.json['fecha_nac'],request.json['a_ingreso'],request.json['estado'],request.json['carrera'],request.json['correo'],request.json['contra'])    
    return jsonify(content)

@estudiante_blueprint.route('/update_estudiante', methods=['PATCH'])
@cross_origin()
def update_estudiante(): #Actualizar los datos de un estudiante
    content = model.update_estudiante(request.json['dni'], request.json['nombres'], request.json['apellidos'],request.json['fecha_nac'],request.json['a_ingreso'],request.json['estado'],request.json['carrera'],request.json['correo'],request.json['contra'])  
    return jsonify(content)

@estudiante_blueprint.route('/delete_estudiante', methods=['POST'])
@cross_origin()
def delete_task(): #Eliminar el registro de un estudiante
    return jsonify(model.delete_estudiante(request.json['dni']))

@estudiante_blueprint.route('/estudiante', methods=['POST'])
@cross_origin()
def task(): #cargar el registro de un estudiante
    return jsonify(model.get_estudiante(request.json['dni']))

@estudiante_blueprint.route('/estudiante_asistencia', methods=['POST'])
@cross_origin()
def asistencia(): #Obtiene si un estudiante tiene una asistencia actual en un curso segun el horario de una clase/sesion
    return jsonify(model.get_estudiante_asistencia(request.json['dni']))

@estudiante_blueprint.route('/estudiante_horario', methods=['POST'])
@cross_origin()
def horario(): #Obtiene el horario de las clases/sesiones de un estudiante por semestre
    return jsonify(model.get_estudiante_horario(request.json['dni'],request.json['semestre']))

@estudiante_blueprint.route('/estudiantes', methods=['POST'])
@cross_origin()
def tasks(): #Carga todos los registros de estudiantes
    return jsonify(model.get_estudiantes())