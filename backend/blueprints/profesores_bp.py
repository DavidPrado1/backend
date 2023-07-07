from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.profesores_model import ProfesorModel
model = ProfesorModel()


profesor_blueprint = Blueprint('profesor_blueprint', __name__)


@profesor_blueprint.route('/create_profesor', methods=['PUT'])
@cross_origin()
def create_profesor(): #Crea un usuario profesor con datos del profesor
    content = model.create_profesor(request.json['dni'], request.json['nombres'], request.json['apellidos'],request.json['fecha_nac'],request.json['fecha_contra'],request.json['estado'],request.json['fecha_fin'],request.json['contra'])    
    return jsonify(content)

@profesor_blueprint.route('/update_profesor', methods=['PATCH'])
@cross_origin()
def update_profesor(): #Actualiza la informacion de un profesor
    content = model.update_profesor(request.json['dni'], request.json['nombres'], request.json['apellidos'],request.json['fecha_nac'],request.json['fecha_contra'],request.json['estado'],request.json['fecha_fin'],request.json['contra'])  
    return jsonify(content)

@profesor_blueprint.route('/delete_profesor', methods=['POST'])
@cross_origin()
def delete_profesor(): #elimina el registro de un profesor
    return jsonify(model.delete_profesor(request.json['dni']))

@profesor_blueprint.route('/profesor', methods=['POST'])
@cross_origin()
def get_profesor(): #Carga los datos de un profesor
    return jsonify(model.get_profesor(request.json['dni']))

@profesor_blueprint.route('/profesores', methods=['POST'])
@cross_origin()
def get_profesores(): #Carga todos los registros de profesores
    return jsonify(model.get_profesores())