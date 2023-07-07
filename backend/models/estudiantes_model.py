from backend.models.connection_pool import MySQLPool
from datetime import datetime


class EstudianteModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_estudiante(self, dni):    
        params = {'dni' : dni}      
        rv = self.con_pool.execute("SELECT estado from estudiantes where dni=%(dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'vector': result[0]}
            data.append(content)
            content = {}
        return data[0]
    
    def get_estudiante_asistencia(self, dni):    
        now = datetime.now()
        print(str(now.strftime("%H:%M")))
        params = {'dni' : dni,
                  'fecha1': str(now.strftime("%Y-%m-%d")),
                    'hora':str(now.strftime("%H:%M"))                  
                  }

        rv = self.con_pool.execute("SELECT c.id, e.estudiante from clases c inner join cursosdesemestre c2 on c.curso = c2.id inner join estudiantescursos e on e.id = c2.id where estudiante = %(dni)s AND fecha=%(fecha1)s AND %(hora)s  BETWEEN hora_inicio and hora_fin",params)                
        
        data = []
        content = {}
        for result in rv:
            content = {'clase': result[0],'estudiante':result[1]}
            data.append(content)
            content = {}
        return data
    
    def get_estudiante_horario(self, dni,semestre):    
        params = {'dni' : dni,
                  'semestre': semestre                  
                  }

        rv = self.con_pool.execute("select c2.curso,c.fecha,c.hora_inicio,c.hora_fin  from clases c inner join cursosdesemestre c2 on c.curso = c2.id inner join estudiantescursos e on e.id = c2.id where estudiante = %(dni)s and semestre = %(semestre)s",params)                
        
        data = []
        content = {}
        for result in rv:
            content = {'name': result[0],'start':result[1] + ' ' + result[2],'end':result[1] + ' ' + result[3]}
            data.append(content)
            content = {}
        return data

 
    

    def get_estudiantes(self):  
        rv = self.con_pool.execute("SELECT dni,nombres,apellidos,fecha_nac,a_ingreso,carrera,correo,contra from estudiantes")  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1],'apellidos': result[2],'fecha_nac': result[3],'a_ingreso': result[4],'carrera': result[5],'correo': result[6],'contra': result[7]}
            data.append(content)
            content = {}
        return data

    def create_estudiante(self, dni, nombres,apellidos,fecha_nac,a_ingreso,estado,carrera,correo,contra):    
        data = {
            'dni' : dni,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'fecha_nac' : fecha_nac,
            'a_ingreso' : a_ingreso,
            'estado' : estado,
            'carrera' : carrera,
            'correo' : correo,
            'contra' : contra
        }  
        query = """insert into estudiantes (dni, nombres,apellidos,fecha_nac,a_ingreso,estado,carrera,correo,contra) 
            values (%(dni)s, %(nombres)s, %(apellidos)s, %(fecha_nac)s, %(a_ingreso)s, %(estado)s, %(carrera)s, %(correo)s,%(contra)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_estudiante(self, dni, nombres,apellidos,fecha_nac,a_ingreso,estado,carrera,correo,contra):    
        data = {
            'dni' : dni,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'fecha_nac' : fecha_nac,
            'a_ingreso' : a_ingreso,
            'estado' : estado,
            'carrera' : carrera,
            'correo' : correo,
            'contra' : contra
        }  
        query = """update estudiantes set nombres = %(nombres)s, apellidos = %(apellidos)s, fecha_nac = %(fecha_nac)s, a_ingreso = %(a_ingreso)s, estado = %(estado)s, carrera = %(carrera)s, correo = %(correo)s, contra = %(contra)s where dni = %(dni)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_estudiante(self, dni):    
        params = {'dni' : dni}      
        query = """delete from estudiantes where dni = %(dni)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


