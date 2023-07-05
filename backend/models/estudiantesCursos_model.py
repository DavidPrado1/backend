from backend.models.connection_pool import MySQLPool

class EstudiantesCursosModel:
    def __init__(self):        
        self.con_pool = MySQLPool()

    def get_estudianteCurso(self, curso,estudiante):    
        params = {'curso' : curso,'estudiante' : estudiante}      
        rv = self.con_pool.execute("SELECT * from estudiantesCursos where curso=%(curso)s and estudiante=%(estudiante)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'curso': result[0], 'estudiante': result[1],'nota1': result[2],'nota2': result[3],'nota3': result[4],'nota4': result[5]}
            data.append(content)
            content = {}
        return data
    

    def get_estudiantesCursos(self,curso): 
        params = {'curso' : curso}    
        rv = self.con_pool.execute("SELECT * from estudiantesCursos where curso=%(curso)s",params)  
        data = []
        content = {}
        for result in rv:
            content = {'curso': result[0], 'estudiante': result[1],'nota1': result[2],'nota2': result[3],'nota3': result[4],'nota4': result[5]}
            data.append(content)
            content = {}
        return data

    def create_estudianteCurso(self, curso,estudiante, nota1,nota2,nota3,nota4):    
        data = {
            'curso' : curso,
            'estudiante' : estudiante,
            'nota1' : nota1,
            'nota2' : nota2,
            'nota3' : nota3,
            'nota4' : nota4
        }  
        query = """insert into estudiantesCursos (curso,estudiante,nota1,nota2,nota3,nota4) 
            values (%(curso)s, %(estudiante)s, %(nota1)s, %(nota2)s, %(nota3)s, %(nota4)s)"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result': 1}
        return result 

    def update_estudianteCurso(self, curso,estudiante, nota1,nota2,nota3,nota4):    
        data = {
            'curso' : curso,
            'estudiante' : estudiante,
            'nota1' : nota1,
            'nota2' : nota2,
            'nota3' : nota3,
            'nota4' : nota4
        }   
        query = """update estudiantesCursos set nota1 = %(nota1)s, nota2 = %(nota2)s, nota3 = %(nota3)s, nota4 = %(nota4)s where curso = %(curso)s and estudiante = %(estudiante)s"""    
        cursor = self.con_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_estudianteCurso(self, curso,estudiante):    
        params = {'curso' : curso,'estudiante':estudiante}      
        query = """delete from estudiantesCursos where curso = %(curso)s and estudiante = %(estudiante)s"""    
        self.con_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


