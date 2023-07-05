from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.estudiantesAbandono_model import EstudianteAbandonoModel
model = EstudianteAbandonoModel()

estudianteAbandono_blueprint = Blueprint('estudianteAbandono_blueprint', __name__)


@estudianteAbandono_blueprint.route('/create_estudianteAbandono', methods=['PUT'])
@cross_origin()
def create_estudianteRetirado():
    content = model.create_estudianteAbandono(request.json['estudiante'], request.json['motivo'], request.json['fecha'])    
    return jsonify(content)


@estudianteAbandono_blueprint.route('/estudianteAbandono', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_estudianteAbandono(request.json['estudiante']))

@estudianteAbandono_blueprint.route('/estudiantesAbandono', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_estudiantesAbandono())