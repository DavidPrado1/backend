from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.estudiantesMatriculados_model import EstudianteMatriculadoModel
model = EstudianteMatriculadoModel()


estudianteMatriculado_blueprint = Blueprint('estudianteMatriculado_blueprint', __name__)

@estudianteMatriculado_blueprint.route('/create_estudianteMatriculado', methods=['PUT'])
@cross_origin()
def create_estudianteMatriculado():
    content = model.create_estudianteMatriculado(request.json['id_estudiante'], request.json['semestre'], request.json['recibo'])    
    return jsonify(content)

@estudianteMatriculado_blueprint.route('/delete_estudianteMatriculado', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_estudianteMatriculado(request.json['id_estudiante'],request.json['semestre']))

@estudianteMatriculado_blueprint.route('/estudianteMatriculado', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_estudianteMatriculado(request.json['id_estudiante'],request.json['semestre']))

@estudianteMatriculado_blueprint.route('/estudiantesMatriculados', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_estudiantesMatriculados(request.json['semestre']))