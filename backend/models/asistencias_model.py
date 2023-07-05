from backend.models.connection_pool import MySQLPool

class AsistenciaModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_asistencia(self, clase,estudiante):    
        params = {'clase' : clase,'estudiante':estudiante}      
        rv = self.con_pool.execute("SELECT * from asistencias where clase=%(clase)s and estudiante=%(estudiante)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'clase': result[0], 'estudiante': result[1]}
            data.append(content)
            content = {}
        return data

    def get_asistencias(self,clase):
        params = {'clase' : clase}  
        rv = self.con_pool.execute("SELECT * from asistencias where clase=%(clase)s",params)  
        data = []
        content = {}
        for result in rv:
            content = {'clase': result[0], 'estudiante': result[1]}
            data.append(content)
            content = {}
        return data

    def create_asistencia(self, clase, estudiante):    
        data = {
            'clase' : clase,
            'estudiante' : estudiante
        }  
        query = """insert into asistencias (clase, estudiante) 
            values (%(clase)s, %(estudiante)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def delete_asistencia(self, clase, estudiante):    
        params = {'clase' : clase,'estudiante':estudiante}      
        query = """delete from asistencias where where clase=%(clase)s and estudiante=%(estudiante)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


