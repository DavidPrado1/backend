from backend.models.connection_pool import MySQLPool

class ClaseModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_clase(self, id):    
        params = {'id' : id}      
        rv = self.con_pool.execute("SELECT * from clases where id=%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'curso': result[1],'fecha': result[2]}
            data.append(content)
            content = {}
        return data

    def get_clases(self):  
        rv = self.con_pool.execute("SELECT * from clases")  
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'curso': result[1],'fecha': result[2],'hora_inicio': result[3],'hora_fin': result[4],'lugar': result[5]}
            data.append(content)
            content = {}
        return data

    def create_clase(self, curso,fecha,hora_inicio,hora_fin,lugar):    
        data = {
            'curso' : curso,
            'fecha' : fecha,
            'hora_inicio': hora_inicio,
            'hora_fin':hora_fin,
            'lugar': lugar,
        }  
        query = """insert into clases (curso,fecha,hora_inicio,hora_fin,lugar) 
            values (%(curso)s, %(fecha)s, %(hora_inicio)s, %(hora_fin)s, %(lugar)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_clase(self, id, curso,fecha):    
        data = {
            'id' : id,
            'curso' : curso,
            'fecha' : fecha
        }   
        query = """update clases set curso = %(curso)s, fecha = %(fecha)s where id = %(id)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_clase(self, id):    
        params = {'id' : id}      
        query = """delete from clases where id = %(id)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


