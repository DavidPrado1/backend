from backend.models.connection_pool import MySQLPool

class AdminModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_admin(self, codigo):    
        params = {'codigo' : codigo}      
        rv = self.con_pool.execute("SELECT * from admin where codigo=%(codigo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'nombres': result[1],'apellidos': result[2],'fecha_inicio': result[3],'contra': result[4]}
            data.append(content)
            content = {}
        return data
    

    def get_admins(self):  
        rv = self.con_pool.execute("SELECT * from admin")  
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'nombres': result[1],'apellidos': result[2],'fecha_inicio': result[3],'contra': result[4]}
            data.append(content)
            content = {}
        return data

    def create_admin(self, codigo, nombres,apellidos,fecha_inicio,contra):    
        data = {
            'codigo' : codigo,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'fecha_inicio' : fecha_inicio,
            'contra' : contra
        }  
        query = """insert into admin (codigo, nombres,apellidos,fecha_inicio,contra) 
            values (%(codigo)s, %(nombres)s, %(apellidos)s, %(fecha_inicio)s, %(contra)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_admin(self, codigo, nombres,apellidos,fecha_inicio,contra):    
        data = {
            'codigo' : codigo,
            'nombres' : nombres,
            'apellidos' : apellidos,
            'fecha_inicio' : fecha_inicio,
            'contra' : contra
        }  
        query = """update admin set nombres = %(nombres)s, apellidos = %(apellidos)s, fecha_inicio = %(fecha_inicio)s, contra = %(contra)s where codigo = %(codigo)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_admin(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from admin where codigo = %(codigo)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


