from backend.models.connection_pool import MySQLPool

class EstudianteMatriculadoModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_estudianteMatriculado(self, id_estudiante,semestre):    
        params = {'id_estudiante' : id_estudiante,'semestre':semestre}      
        rv = self.con_pool.execute("SELECT * from estudiantesMatriculados where id_estudiante=%(id_estudiante)s and semestre=%(semestre)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_estudiante': result[0], 'semestre': result[1],'recibo': result[2]}
            data.append(content)
            content = {}
        return data

    def get_estudiantesMatriculados(self,semestre): 
        params = {'semestre':semestre}  
        rv = self.con_pool.execute("SELECT * from estudiantesMatriculados where semestre=%(semestre)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_estudiante': result[0], 'semestre': result[1],'recibo': result[2]}
            data.append(content)
            content = {}
        return data

    def create_estudianteMatriculado(self, id_estudiante, semestre,recibo):    
        data = {
            'id_estudiante' : id_estudiante,
            'semestre' : semestre,
            'recibo' : recibo
        }  
        query = """insert into estudiantesMatriculados (id_estudiante, semestre,recibo) 
            values (%(id_estudiante)s, %(semestre)s, %(recibo)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def delete_estudianteMatriculado(self, id_estudiante,semestre):    
        params = {'id_estudiante' : id_estudiante,'semestre':semestre}      
        query = """delete from estudiantesMatriculados where id_estudiante = %(id_estudiante)s and semestre = %(semestre)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


