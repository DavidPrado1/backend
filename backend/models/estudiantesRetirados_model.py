from backend.models.connection_pool import MySQLPool

class EstudianteRetiradoModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_estudianteRetirado(self, estudiante):    
        params = {'estudiante' : estudiante}      
        rv = self.con_pool.execute("SELECT * from estudiantesRetirados where estudiante=%(estudiante)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'estudiante': result[0], 'motivo': result[1],'fecha': result[2]}
            data.append(content)
            content = {}
        return data

    def get_estudiantesRetirados(self):  
        rv = self.con_pool.execute("SELECT * from estudiantesRetirados")  
        data = []
        content = {}
        for result in rv:
            content = {'estudiante': result[0], 'motivo': result[1],'fecha': result[2]}
            data.append(content)
            content = {}
        return data

    def create_estudianteRetirado(self, estudiante, motivo,fecha):    
        data = {
            'estudiante' : estudiante,
            'motivo' : motivo,
            'fecha' : fecha
        }  
        query = """insert into estudiantesRetirados (estudiante, motivo,fecha) 
            values (%(estudiante)s, %(motivo)s, %(fecha)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

