from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.justificaciones_model import JustificacionModel
model = JustificacionModel()

justificacion_blueprint = Blueprint('justificacion_blueprint', __name__)


@justificacion_blueprint.route('/justificacion', methods=['PUT'])
@cross_origin()
def create_justificacion():
    content = model.create_justificacion(request.json['estudiante'], request.json['clase'], request.json['justificacion'],request.json['fecha'],request.json['estado'])    
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['PATCH'])
@cross_origin()
def update_justificacion():
    content = model.update_justificacion(request.json['estudiante'], request.json['clase'], request.json['justificacion'],request.json['fecha'],request.json['estado'])  
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['DELETE'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_justificacion(request.json['estudiante'],request.json['clase']))

@justificacion_blueprint.route('/justificacion', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_justificacion(request.json['estudiante'],request.json['clase']))

@justificacion_blueprint.route('/justificaciones', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_justificaciones(request.json['estudiante']))