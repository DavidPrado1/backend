from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.clases_model import ClaseModel
model = ClaseModel()

clase_blueprint = Blueprint('clase_blueprint', __name__)

@clase_blueprint.route('/clase', methods=['PUT'])
@cross_origin()
def create_clase(): #Crear una clase/sesion de un curso
    content = model.create_clase(request.json['id'], request.json['curso'], request.json['fecha'],request.json['hora_inicio'],request.json['hora_fin'],request.json['lugar'])   
    return jsonify(content)

@clase_blueprint.route('/clase', methods=['DELETE'])
@cross_origin()
def delete_task(): #Eliminar una clase/sesion de un curso
    return jsonify(model.delete_clase(request.json['id']))

@clase_blueprint.route('/clase', methods=['POST'])
@cross_origin()
def task(): #Cargar los datos de una clase/sesion
    return jsonify(model.get_clase(request.json['id']))

@clase_blueprint.route('/clases', methods=['POST'])
@cross_origin()
def tasks(): #Cargar todas las clases/sesiones
    return jsonify(model.get_clases())