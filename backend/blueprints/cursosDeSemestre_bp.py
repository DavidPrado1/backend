from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.cursosDeSemestre_model import CursoDeSemestreModel
model = CursoDeSemestreModel()



cursoDeSemestre_blueprint = Blueprint('cursoDeSemestre_blueprint', __name__)

@cursoDeSemestre_blueprint.route('/create_cursoDeSemestre', methods=['PUT'])
@cross_origin()
def create_cursoDeSemestre():
    content = model.create_cursoDeSemestre(request.json['semestre'], request.json['curso'], request.json['profesor'],request.json['fecha_inicio'],request.json['fecha_fin'])    
    return jsonify(content)

@cursoDeSemestre_blueprint.route('/update_cursoDeSemestre', methods=['PATCH'])
@cross_origin()
def update_cursoDeSemestre():
    content = model.update_cursoDeSemestre(request.json['semestre'], request.json['curso'], request.json['profesor'],request.json['fecha_inicio'],request.json['fecha_fin'])  
    return jsonify(content)

@cursoDeSemestre_blueprint.route('/delete_cursoDeSemestre', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_cursoDeSemestre(request.json['id']))

@cursoDeSemestre_blueprint.route('/cursoDeSemestre', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_cursoDeSemestre(request.json['semestre'],request.json['curso']))

@cursoDeSemestre_blueprint.route('/cursosDeSemestres', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_cursosDeSemestre(request.json['semestre']))