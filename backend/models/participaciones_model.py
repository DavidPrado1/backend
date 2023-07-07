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
            content = {'clase': result[0], 'estudiante': result[1],'cant': result[2]}
            data.append(content)
            content = {}
        return data
    
    def create_participacion(self, clase,estudiante):    
        data = {
            'clase' : clase,
            'estudiante' : estudiante,
            'cant' : 1
        } 
        query = """insert into participaciones (clase, estudiante,cant) 
            values (%(clase)s, %(estudiante)s, %(cant)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 
    
    def sum_participacion(self, clase,estudiante):    
        data = {
            'clase' : clase,
            'estudiante' : estudiante,
        } 
        query = """update participaciones set cant = cant +  1 where estudiante = %(estudiante)s and clase = %(clase)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)    

        result = {'result': 1}
        return result
    
    def res_participacion(self, clase,estudiante):    
        data = {
            'clase' : clase,
            'estudiante' : estudiante,
        } 
        query = """update participaciones set cant = cant -  1 where estudiante = %(estudiante)s and clase = %(clase)s and cant > 0"""    
        cursor = self.con_pool.execute(query, data, commit=True)     

        result = {'result': 1}
        return result 


