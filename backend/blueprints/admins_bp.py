from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.admins_model import AdminModel
model = AdminModel()



admin_blueprint = Blueprint('admin_blueprint', __name__)


@admin_blueprint.route('/admin', methods=['PUT'])
@cross_origin()
def create_admin():
    content = model.create_admin(request.json['codigo'], request.json['nombres'], request.json['apellidos'],request.json['fecha_inicio'],request.json['contra'])    
    return jsonify(content)

@admin_blueprint.route('/admin', methods=['PATCH'])
@cross_origin()
def update_admin():
    content = model.update_admin(request.json['codigo'], request.json['nombres'], request.json['apellidos'],request.json['fecha_inicio'],request.json['contra'])  
    return jsonify(content)

@admin_blueprint.route('/admin', methods=['DELETE'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_admin(request.json['codigo']))

@admin_blueprint.route('/admin', methods=['POST'])
@cross_origin()
def task():
    return jsonify(model.get_admin(request.json['codigo']))

@admin_blueprint.route('/admins', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_admins())