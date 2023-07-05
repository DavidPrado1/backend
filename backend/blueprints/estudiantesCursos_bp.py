from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.estudiantesCursos_model import EstudiantesCursosModel
model = EstudiantesCursosModel()


estudianteCurso_blueprint = Blueprint('estudianteCurso_blueprint', __name__)

@estudianteCurso_blueprint.route('/estudianteCurso', methods=['PUT'])
@cross_origin()
def create_estudianteCurso():
    content = model.create_estudianteCurso(request.json['curso'], request.json['estudiante'], request.json['nota1'],request.json['nota2'],request.json['nota3'],request.json['nota4'])   
    return jsonify(content)

@estudianteCurso_blueprint.route('/estudianteCurso', methods=['PATCH'])
@cross_origin()
def update_estudianteCurso():
    content = model.update_estudianteCurso(request.json['curso'], request.json['estudiante'], request.json['nota1'],request.json['nota2'],request.json['nota3'],request.json['nota4'])  
    return jsonify(content)

@estudianteCurso_blueprint.route('/estudianteCurso', methods=['DELETE'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_estudianteCurso(request.json['curso'],request.json['estudiante']))

@estudianteCurso_blueprint.route('/estudianteCurso', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_estudianteCurso(request.json['curso'],request.json['estudiante']))

@estudianteCurso_blueprint.route('/estudiantesCursos', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_cursosDecurso(request.json['curso']))