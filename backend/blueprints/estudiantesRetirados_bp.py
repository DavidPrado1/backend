from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.estudiantesRetirados_model import EstudianteRetiradoModel
model = EstudianteRetiradoModel()

estudianteRetirado_blueprint = Blueprint('estudianteRetirado_blueprint', __name__)


@estudianteRetirado_blueprint.route('/create_estudianteRetirado', methods=['PUT'])
@cross_origin()
def create_estudianteRetirado():
    content = model.create_estudianteRetirado(request.json['estudiante'], request.json['motivo'], request.json['fecha'])    
    return jsonify(content)


@estudianteRetirado_blueprint.route('/estudianteRetirado', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_estudianteRetirado(request.json['estudiante']))

@estudianteRetirado_blueprint.route('/estudiantesRetirados', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_estudiantesRetirados())