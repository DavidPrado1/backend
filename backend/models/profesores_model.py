from backend.models.connection_pool import MySQLPool

class ProfesorModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_profesor(self, dni):    
        params = {'dni' : dni}      
        rv = self.con_pool.execute("SELECT * from profesores where dni=%(dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1],'apellidos': result[2],'fecha_nac': result[3],'fecha_contra': result[4],'estado': result[5],'fecha_fin': result[6],'contra': result[7]}
            data.append(content)
            content = {}
        return data
    

    def get_profesores(self):  
        rv = self.con_pool.execute("SELECT * from profesores")  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1],'apellidos': result[2],'fecha_nac': result[3],'fecha_contra': result[4],'estado': result[5],'fecha_fin': result[6],'contra': result[7]}
            data.append(content)
            content = {}
        return data

    def create_profesor(self, dni, nombres,apellidos,fecha_nac,fecha_contra,estado,fecha_fin,contra):    
        data = {
            'dni' : dni,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'fecha_nac' : fecha_nac,
            'fecha_contra' : fecha_contra,
            'estado' : estado,
            'fecha_fin' : fecha_fin,
            'contra' : contra
        }  
        query = """insert into profesores (dni, nombres,apellidos,fecha_nac,fecha_contra,estado,fecha_fin,contra) 
            values (%(dni)s, %(nombres)s, %(apellidos)s, %(fecha_nac)s, %(fecha_contra)s, %(estado)s, %(fecha_fin)s, %(contra)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_profesor(self, dni, nombres,apellidos,fecha_nac,fecha_contra,estado,fecha_fin,contra):    
        data = {
            'dni' : dni,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'fecha_nac' : fecha_nac,
            'fecha_contra' : fecha_contra,
            'estado' : estado,
            'fecha_fin' : fecha_fin,
            'contra' : contra
        }  
        query = """update profesores set nombres = %(nombres)s, apellidos = %(apellidos)s, fecha_nac = %(fecha_nac)s, fecha_contra = %(fecha_contra)s, estado = %(estado)s, fecha_fin = %(fecha_fin)s, contra = %(contra)s where dni = %(dni)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_profesor(self, dni):    
        params = {'dni' : dni}      
        query = """delete from profesores where dni = %(dni)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


