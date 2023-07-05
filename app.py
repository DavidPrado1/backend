from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.estudiantes_bp import estudiante_blueprint
from backend.blueprints.profesores_bp import profesor_blueprint
from backend.blueprints.admins_bp import admin_blueprint
from backend.blueprints.semestres_bp import semestre_blueprint
from backend.blueprints.clases_bp import clase_blueprint
from backend.blueprints.cursos_bp import curso_blueprint
from backend.blueprints.asistencias_bp import asistencia_blueprint
from backend.blueprints.cursosDeSemestre_bp import cursoDeSemestre_blueprint
from backend.blueprints.estudiantesAbandono_bp import estudianteAbandono_blueprint
from backend.blueprints.estudiantesCursos_bp import estudianteCurso_blueprint
from backend.blueprints.estudiantesMatriculados_bp import estudianteMatriculado_blueprint
from backend.blueprints.estudiantesRetirados_bp import estudianteRetirado_blueprint
from backend.blueprints.horarios_bp import horario_blueprint
from backend.blueprints.justificaciones_bp import justificacion_blueprint
from backend.blueprints.participaciones_bp import participacion_blueprint



app = Flask(__name__)

app.register_blueprint(estudiante_blueprint)
app.register_blueprint(profesor_blueprint)
app.register_blueprint(asistencia_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(semestre_blueprint)
app.register_blueprint(clase_blueprint)
app.register_blueprint(curso_blueprint)
app.register_blueprint(cursoDeSemestre_blueprint)
app.register_blueprint(estudianteAbandono_blueprint)
app.register_blueprint(estudianteCurso_blueprint)
app.register_blueprint(estudianteRetirado_blueprint)
app.register_blueprint(estudianteMatriculado_blueprint)
app.register_blueprint(horario_blueprint)
app.register_blueprint(justificacion_blueprint)
app.register_blueprint(participacion_blueprint)



cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)