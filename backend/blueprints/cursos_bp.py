from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.cursos_model import CursoModel
model = CursoModel()



curso_blueprint = Blueprint('curso_blueprint', __name__)

@curso_blueprint.route('/create_curso', methods=['PUT'])
@cross_origin()
def create_curso(): #Crear un nuevo curso
    content = model.create_curso(request.json['nombreCurso'], request.json['cursoPrerequisito'], request.json['descripcion'])    
    return jsonify(content)

@curso_blueprint.route('/delete_curso', methods=['POST'])
@cross_origin()
def delete_task(): #Eliminar un nuevo curso
    return jsonify(model.delete_curso(request.json['nombreCurso']))

@curso_blueprint.route('/curso', methods=['POST'])
@cross_origin()
def task(): #Cargar los datps de un curso
    return jsonify(model.get_curso(request.json['nombreCurso']))

@curso_blueprint.route('/cursos', methods=['POST'])
@cross_origin()
def tasks(): #Cargar todos los cursos
    return jsonify(model.get_cursos())

@curso_blueprint.route('/cursosnames', methods=['POST'])
@cross_origin()
def tasks2(): #Cargar solo los nombres de los cursos
    return jsonify(model.get_cursosnames())