from backend.models.connection_pool import MySQLPool

class ParticipacionModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_participacion(self, estudiante,clase):    
        params = {'estudiante' : estudiante,'clase':clase}      
        rv = self.con_pool.execute("SELECT * from participaciones where estudiante=%(estudiante)s and clase=%(clase)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'num': result[0], 'estudiante': result[1],'clase': result[2]}
            data.append(content)
            content = {}
        return data

    def get_participaciones(self,clase):  
        params = {'clase':clase}
        rv = self.con_pool.execute("SELECT * from participaciones where clase=%(clase)s",params)  
        data = []
        content = {}
        for result in rv:
            content = {'num': result[0], 'estudiante': result[1],'clase': result[2]}
            data.append(content)
            content = {}
        return data

    def create_participacion(self, num, estudiante,clase):    
        data = {
            'num' : num,
            'estudiante' : estudiante,
            'clase' : clase
        }  
        query = """insert into participaciones (num, estudiante,clase) 
            values (%(num)s, %(estudiante)s, %(clase)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 


