# Computación Distribuida - Clúster

##Pasos para desplegar la aplicacion:
                
----
Crear una Base de Datos MySQL con el siguiente script:
```javascript
CREATE TABLE estudiantes (
  dni varchar(8) PRIMARY KEY,
  nombres varchar(255),
  apellidos varchar(255),
  fecha_nac date,
  a_ingreso date,
  estado varchar(255),
  carrera varchar(255),
  correo varchar(255),
  contra varchar(255)
);

CREATE TABLE profesores (
  dni varchar(8) PRIMARY KEY,
  nombres varchar(255),
  apellidos varchar(255),
  fecha_nac date,
  fecha_contra date,
  estado varchar(255),
  fecha_fin date,
  contra varchar(255)
);

CREATE TABLE admin (
  codigo varchar(4) PRIMARY KEY,
  nombres varchar(255),
  apellidos varchar(255),
  fecha_inicio date,
  contra varchar(255)
);

CREATE TABLE semestres (
  codigo varchar(255) PRIMARY KEY
);

CREATE TABLE estudiantesMatriculados (
  id_estudiante varchar(8),
  semestre varchar(255),
  recibo varchar(255),
  PRIMARY KEY (id_estudiante, semestre)
);

CREATE TABLE cursos (
  nombreCurso varchar(255) PRIMARY KEY,
  cursoPrerequisito varchar(255),
  descripcion text
);

CREATE TABLE cursosDeSemestre (
  semestre varchar(255),
  curso varchar(255),
  profesor varchar(255),
  fecha_inicio date,
  fecha_fin date,
  PRIMARY KEY (semestre, curso)
);

CREATE TABLE estudiantesCursos (
  curso varchar(255),
  estudiante varchar(255),
  nota1 decimal(4,2),
  nota2 decimal(4,2),
  nota3 decimal(4,2),
  nota4 decimal(4,2),
  PRIMARY KEY (curso, estudiante)
);

CREATE TABLE horarios (
  n_dia varchar(255),
  curso varchar(255),
  horas varchar(255),
  dia varchar(255),
  PRIMARY KEY (n_dia, curso)
);

CREATE TABLE clases (
  id varchar(15) PRIMARY KEY,
  curso varchar(255),
  fecha date,
  lugar varchar(255)
);

CREATE TABLE asistencias (
  clase varchar(15),
  estudiante varchar(8),
  PRIMARY KEY (clase, estudiante)
);

CREATE TABLE justificaciones (
  estudiante varchar(8),
  clase varchar(15),
  justificacion int,
  fecha date,
  estado boolean,
  PRIMARY KEY (estudiante, clase)
);

CREATE TABLE participaciones (
  num integer,
  estudiante varchar(8),
  clase varchar(15),
  PRIMARY KEY (num, estudiante, clase)
);

CREATE TABLE estudiantesRetirados (
  estudiante varchar(8) PRIMARY KEY,
  motivo varchar(255),
  fecha date
);

CREATE TABLE estudiantesAbandono (
  estudiante varchar(8) PRIMARY KEY,
  motivo varchar(255),
  fecha date
);

ALTER TABLE estudiantesMatriculados ADD FOREIGN KEY (semestre) REFERENCES semestres (codigo);

ALTER TABLE cursos ADD FOREIGN KEY (cursoPrerequisito) REFERENCES cursos (nombreCurso);

ALTER TABLE cursosDeSemestre ADD FOREIGN KEY (semestre) REFERENCES semestres (codigo);

ALTER TABLE cursosDeSemestre ADD FOREIGN KEY (curso) REFERENCES cursos (nombreCurso);

ALTER TABLE cursosDeSemestre ADD FOREIGN KEY (profesor) REFERENCES profesores (dni);

ALTER TABLE estudiantesCursos ADD FOREIGN KEY (curso) REFERENCES cursos (nombreCurso);

ALTER TABLE estudiantesCursos ADD FOREIGN KEY (estudiante) REFERENCES estudiantes (dni);

ALTER TABLE horarios ADD FOREIGN KEY (curso) REFERENCES cursos (nombreCurso);

ALTER TABLE clases ADD FOREIGN KEY (curso) REFERENCES cursos (nombreCurso);

ALTER TABLE asistencias ADD FOREIGN KEY (clase) REFERENCES clases (id);

ALTER TABLE justificaciones ADD FOREIGN KEY (clase) REFERENCES clases (id);

ALTER TABLE justificaciones ADD FOREIGN KEY (estudiante) REFERENCES estudiantes (dni);

ALTER TABLE participaciones ADD FOREIGN KEY (clase) REFERENCES clases (id);

ALTER TABLE participaciones ADD FOREIGN KEY (estudiante) REFERENCES estudiantes (dni);
sele
ALTER TABLE estudiantesRetirados ADD FOREIGN KEY (estudiante) REFERENCES estudiantes (dni);

ALTER TABLE estudiantesAbandono ADD FOREIGN KEY (estudiante) REFERENCES estudiantes (dni);


```


##Librerias Necesarias:
                
----
`Flask`
`Flask - Cors`
`PyMySQL`
`SQL-Alchemy`
`mysql-connector-python`
`marshmallow-sqlalchemy`
`flask-marshmallow`
`flask-sqlalchemy`


                
----

##Configuración del archivo de inicialización:
                
----
Crear un archivo .ini para la configuracion de parametros de conexion en la base de datos  del connection pool de la aplicacion.

`backend/models/connection_pool.py`

Este mismo puede estar ubicado en cualquier parte del servidos, solo hacer referencia a su ubicacion en el connection_pool.
                
----

##Despliegue de la Aplicación:
                
----
Solo correr el archivo app.py.
`python app.py`
