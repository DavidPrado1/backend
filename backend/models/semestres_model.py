from backend.models.connection_pool import MySQLPool

class SemestreModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_semestre(self, codigo):    
        params = {'codigo' : codigo}      
        rv = self.con_pool.execute("SELECT * from semestres where codigo=%(codigo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0]}
            data.append(content)
            content = {}
        return data
    

    def get_semestres(self):  
        rv = self.con_pool.execute("SELECT * from semestres")  
        data = []
        for result in rv:
            data.append(result[0])

        return data
    
    

    def create_semestre(self, codigo):    
        data = {
            'codigo' : codigo
        }  
        query = """insert into semestres (codigo) 
            values (%(codigo)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 
    
    def delete_semestre(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from semestres where codigo = %(codigo)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


