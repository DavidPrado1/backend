from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.asistencias_model import AsistenciaModel
model = AsistenciaModel()

asistencia_blueprint = Blueprint('asistencia_blueprint', __name__)

@asistencia_blueprint.route('/asistencia', methods=['PUT'])
@cross_origin()
def create_asistencia(): #Registrar asistencia
    content = model.create_asistencia(request.json['clase'], request.json['estudiante'])   
    return jsonify(content)

@asistencia_blueprint.route('/asistencia', methods=['DELETE'])
@cross_origin()
def delete_task(): #Eliminar asistencia
    return jsonify(model.delete_asistencia(request.json['clase'],request.json['estudiante']))

@asistencia_blueprint.route('/asistencia', methods=['POST'])
@cross_origin()
def task(): #Cargar asistencias de una clase/sesion segun el estudiante
    return jsonify(model.get_asistencia(request.json['clase'],request.json['estudiante']))

@asistencia_blueprint.route('/asistencias', methods=['POST'])
@cross_origin()
def tasks(): #Cargar todas las asistencias de una clase/sesion
    return jsonify(model.get_asistencias(request.json['clase']))

