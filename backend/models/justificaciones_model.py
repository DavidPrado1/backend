from backend.models.connection_pool import MySQLPool

class JustificacionModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_justificacion(self, estudiante,clase):    
        params = {'estudiante' : estudiante,'clase' : clase}      
        rv = self.con_pool.execute("SELECT * from justificaciones where estudiante=%(estudiante)s and clase=%(clase)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'estudiante': result[0], 'clase': result[1],'justificacion': result[2],'fecha': result[3],'estado': result[4]}
            data.append(content)
            content = {}
        return data
    

    def get_justificaciones(self,estudiante): 
        params = {'estudiante' : estudiante}    
        rv = self.con_pool.execute("SELECT * from justificaciones where estudiante=%(estudiante)s",params)  
        data = []
        content = {}
        for result in rv:
            content = {'estudiante': result[0], 'clase': result[1],'justificacion': result[2],'fecha': result[3],'estado': result[4]}
            data.append(content)
            content = {}
        return data

    def create_justificacion(self, estudiante, clase,justificacion,fecha,estado):    
        data = {
            'estudiante' : estudiante,
            'clase' : clase,
            'justificacion' : justificacion,
            'fecha' : fecha,
            'estado' : estado
        }  
        query = """insert into justificaciones (estudiante, clase,justificacion,fecha,estado) 
            values (%(estudiante)s, %(clase)s, %(justificacion)s, %(fecha)s, %(estado)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_justificacion(self, estudiante, clase,justificacion,fecha,estado):    
        data = {
            'estudiante' : estudiante,
            'clase' : clase,
            'justificacion' : justificacion,
            'fecha' : fecha,
            'estado' : estado
        }  
        query = """update justificaciones set justificacion = %(justificacion)s, fecha = %(fecha)s, estado = %(estado)s where estudiante = %(estudiante)s and clase = %(clase)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_justificacion(self, estudiante, clase):    
        params = {'estudiante' : estudiante,'curso':clase}      
        query = """delete from justificaciones where estudiante = %(estudiante)s and clase = %(clase)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


