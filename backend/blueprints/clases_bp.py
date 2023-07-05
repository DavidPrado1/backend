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
def create_clase():
    content = model.create_clase(request.json['id'], request.json['curso'], request.json['fecha'],request.json['hora_inicio'],request.json['hora_fin'],request.json['lugar'])   
    return jsonify(content)

@clase_blueprint.route('/clase', methods=['PATCH'])
@cross_origin()
def update_clase():
    content = model.update_clase(request.json['id'], request.json['curso'], request.json['fecha'],request.json['lugar'])   
    return jsonify(content)

@clase_blueprint.route('/clase', methods=['DELETE'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_clase(request.json['id']))

@clase_blueprint.route('/clase', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_clase(request.json['id']))

@clase_blueprint.route('/clases', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_clases())