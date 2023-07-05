from backend.models.connection_pool import MySQLPool

class HorarioModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_horario(self, n_dia,curso):    
        params = {'n_dia' : n_dia,'curso' : curso}      
        rv = self.con_pool.execute("SELECT * from horarios where n_dia=%(n_dia)s and curso=%(curso)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'n_dia': result[0], 'curso': result[1],'horas': result[2],'dia': result[3]}
            data.append(content)
            content = {}
        return data
    

    def get_horarios(self,curso): 
        params = {'curso' : curso}    
        rv = self.con_pool.execute("SELECT * from horarios where curso=%(curso)s",params)  
        data = []
        content = {}
        for result in rv:
            content = {'n_dia': result[0], 'curso': result[1],'horas': result[2],'dia': result[3]}
            data.append(content)
            content = {}
        return data

    def create_horario(self, n_dia,curso,horas,dia):    
        data = {
            'n_dia' : n_dia,
            'curso' : curso,
            'horas' : horas,
            'dia' : dia
        }  
        query = """insert into horarios (n_dia,curso,horas,dia) 
            values (%(n_dia)s, %(curso)s, %(horas)s, %(dia)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_horario(self, n_dia,curso,horas,dia):    
        data = {
            'n_dia' : n_dia,
            'curso' : curso,
            'horas' : horas,
            'dia' : dia
        } 
        query = """update horarios set horas = %(horas)s, dia = %(dia)s where n_dia = %(n_dia)s and curso = %(curso)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_horario(self, n_dia,curso):    
        params = {'n_dia' : n_dia,'curso':curso}      
        query = """delete from horarios where n_dia = %(n_dia)s and curso = %(curso)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


