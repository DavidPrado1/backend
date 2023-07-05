from backend.models.connection_pool import MySQLPool

class EstudianteAbandonoModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_estudianteAbandono(self, estudiante):    
        params = {'estudiante' : estudiante}      
        rv = self.con_pool.execute("SELECT * from estudiantesAbandono where estudiante=%(estudiante)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'estudiante': result[0], 'motivo': result[1],'fecha': result[2]}
            data.append(content)
            content = {}
        return data

    def get_estudiantesAbandono(self):  
        rv = self.con_pool.execute("SELECT * from estudiantesAbandono")  
        data = []
        content = {}
        for result in rv:
            content = {'estudiante': result[0], 'motivo': result[1],'fecha': result[2]}
            data.append(content)
            content = {}
        return data

    def create_estudianteAbandono(self, estudiante, motivo,fecha):    
        data = {
            'estudiante' : estudiante,
            'motivo' : motivo,
            'fecha' : fecha
        }  
        query = """insert into estudiantesAbandono (estudiante, motivo,fecha) 
            values (%(estudiante)s, %(motivo)s, %(fecha)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

