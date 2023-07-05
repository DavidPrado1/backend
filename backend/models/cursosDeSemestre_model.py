from backend.models.connection_pool import MySQLPool

class CursoDeSemestreModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_cursoDeSemestre(self, semestre,curso):    
        params = {'semestre' : semestre,'curso' : curso}      
        rv = self.con_pool.execute("SELECT * from cursosDeSemestre where semestre=%(semestre)s and curso=%(curso)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'semestre': result[0], 'curso': result[1],'profesor': result[2],'fecha_inicio': result[3],'fecha_fin': result[4]}
            data.append(content)
            content = {}
        return data
    

    def get_cursosDeSemestre(self,semestre): 
        params = {'semestre' : semestre}    
        rv = self.con_pool.execute("SELECT * from cursosDeSemestre where semestre=%(semestre)s",params)  
        data = []
        content = {}
        for result in rv:
            content = {'id':result[0],'semestre':result[1],'curso': result[2],'profesor': result[3],'fecha_inicio': result[4],'fecha_fin': result[5]}
            data.append(content)
            content = {}
        return data

    def create_cursoDeSemestre(self, semestre, curso,profesor,fecha_inicio,fecha_fin):    
        data = {
            'semestre' : semestre,
            'curso' : curso,
            'profesor' : profesor,
            'fecha_inicio' : fecha_inicio,
            'fecha_fin' : fecha_fin
        }  
        query = """insert into cursosDeSemestre (semestre, curso,profesor,fecha_inicio,fecha_fin) 
            values (%(semestre)s, %(curso)s, %(profesor)s, %(fecha_inicio)s, %(fecha_fin)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_cursoDeSemestre(self, semestre, curso,profesor,fecha_inicio,fecha_fin):    
        data = {
            'semestre' : semestre,
            'curso' : curso,
            'profesor' : profesor,
            'fecha_inicio' : fecha_inicio,
            'fecha_fin' : fecha_fin
        }  
        query = """update cursosDeSemestre set profesor = %(profesor)s, fecha_inicio = %(fecha_inicio)s, fecha_fin = %(fecha_fin)s where semestre = %(semestre)s and curso = %(curso)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_cursoDeSemestre(self, id):    
        params = {'id' : id}      
        query = """delete from cursosDeSemestre where semestre = %(id)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


