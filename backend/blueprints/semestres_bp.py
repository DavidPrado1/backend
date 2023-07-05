from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.semestres_model import SemestreModel
model = SemestreModel()



semestre_blueprint = Blueprint('semestre_blueprint', __name__)


@semestre_blueprint.route('/semestre', methods=['PUT'])
@cross_origin()
def create_semestre():
    content = model.create_semestre(request.json['codigo'])    
    return jsonify(content)

@semestre_blueprint.route('/semestre', methods=['DELETE'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_semestre(request.json['codigo']))

@semestre_blueprint.route('/semestre', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_semestre(request.json['codigo']))

@semestre_blueprint.route('/semestres', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_semestres())