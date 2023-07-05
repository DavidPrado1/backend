from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.horarios_model import HorarioModel
model = HorarioModel()


horario_blueprint = Blueprint('horario_blueprint', __name__)

@horario_blueprint.route('/horario', methods=['PUT'])
@cross_origin()
def create_horario():
    content = model.create_horario(request.json['n_dia'], request.json['curso'], request.json['horas'],request.json['dia'])   
    return jsonify(content)

@horario_blueprint.route('/horario', methods=['PATCH'])
@cross_origin()
def update_horario():
    content = model.update_horario(request.json['n_dia'], request.json['curso'], request.json['horas'],request.json['dia'])   
    return jsonify(content)

@horario_blueprint.route('/horario', methods=['DELETE'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_horario(request.json['n_dia'],request.json['curso']))

@horario_blueprint.route('/horario', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_horario(request.json['n_dia'],request.json['curso']))

@horario_blueprint.route('/horarios', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_horarios(request.json['curso']))