from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.participaciones_model import ParticipacionModel
model = ParticipacionModel()

participacion_blueprint = Blueprint('participacion_blueprint', __name__)


@participacion_blueprint.route('/participacion', methods=['PUT'])
@cross_origin()
def create_participacion():
    content = model.create_participacion(request.json['num'], request.json['estudiante'], request.json['clase'])    
    return jsonify(content)


@participacion_blueprint.route('/participacion', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_participacion(request.json['estudiante'],request.json['clase']))

@participacion_blueprint.route('/participaciones', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_participaciones(request.json['clase']))