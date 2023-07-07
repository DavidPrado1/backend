from backend.models.connection_pool import MySQLPool

class CursoModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_curso(self, nombreCurso):    
        params = {'nombreCurso' : nombreCurso}      
        rv = self.con_pool.execute("SELECT * from cursos where nombreCurso=%(nombreCurso)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'nombreCurso': result[0], 'cursoPrerequisito': result[1],'descripcion': result[2]}
            data.append(content)
            content = {}
        return data

    def get_cursosnames(self):  #Obtiene todos los nombres (son primary key) de la tabla curso
        rv = self.con_pool.execute("SELECT nombreCurso from cursos")  
        data = []
        for result in rv:
            data.append(result[0])
        return data

    def get_cursos(self):  
        rv = self.con_pool.execute("SELECT * from cursos")  
        data = []
        content = {}
        for result in rv:
            content = {'nombreCurso': result[0], 'cursoPrerequisito': result[1],'descripcion': result[2]}
            data.append(content)
            content = {}
        return data

    def create_curso(self, nombreCurso, cursoPrerequisito,descripcion):    
        data = {
            'nombreCurso' : nombreCurso,
            'cursoPrerequisito' : cursoPrerequisito,
            'descripcion' : descripcion
        }  
        query = """insert into cursos (nombreCurso, cursoPrerequisito,descripcion) 
            values (%(nombreCurso)s, %(cursoPrerequisito)s, %(descripcion)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_curso(self, nombreCurso, cursoPrerequisito,descripcion):    
        data = {
            'nombreCurso' : nombreCurso,
            'cursoPrerequisito' : cursoPrerequisito,
            'descripcion' : descripcion
        }  
        query = """update cursos set cursoPrerequisito = %(cursoPrerequisito)s, descripcion = %(descripcion)s where nombreCurso = %(nombreCurso)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_curso(self, nombreCurso):    
        params = {'nombreCurso' : nombreCurso}      
        query = """delete from cursos where nombreCurso = %(nombreCurso)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


