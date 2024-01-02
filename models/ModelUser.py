from connectionPool.pool import MySQLPool

class UserModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_user_username(self, email):
        params = {'email': email}
        rv = self.mysql_pool.execute(
            "SELECT * from user where email=%(email)s", params)
        content = {}
        for result in rv:
            content = {
                'email': result[0], 'password': result[1], 'firstName': result[2], 'lastName': result[3]}
            return content
        return None
    
    def add_user(self, data: dict):
        params = {
            'email' : data["email"],
            'password' : data["password"],
            'firtsName' : data["firstname"],
            'lastName' : data["lastname"],
        }

        query = """insert into user (email, password, firstName, lastName)
            values (%(email)s, %(password)s, %(firtsName)s, %(lastName)s)"""    

        cursor = self.mysql_pool.execute(query, params, commit=True)

        return cursor
    
# Example model
    def get_evaluate_count(self):
        sql = """
        SELECT 
            COUNT(*) AS total_registros,
            SUM(CASE WHEN value = 'good' THEN 1 ELSE 0 END) AS good_count,
            SUM(CASE WHEN value = 'neutral' THEN 1 ELSE 0 END) AS neutral_count,
            SUM(CASE WHEN value = 'bad' THEN 1 ELSE 0 END) AS bad_count 
        FROM evaluate
        """
        
        result = self.mysql_pool.execute(sql)

        if result:
            result_dict = {
                'total_registros': result[0][0],
                'good_count': result[0][1],
                'neutral_count': result[0][2],
                'bad_count': result[0][3]
            }
            return result_dict
        return {
            'total_registros': 0,
            'good_count': 0,
            'neutral_count': 0,
            'bad_count': 0
        }

########################## Podible Admin CRUD ################################

    # Funcion para obtener un administrador por su ID
    def get_administrador(self, id_adm):
        params = {'id_adm' : id_adm}      
        rv = self.mysql_pool.execute("SELECT * from administrador where id_adm=%(id_adm)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_adm': result[0], 'rol': result[1]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para obtener todos los administradores
    def get_administradors(self):
        rv = self.mysql_pool.execute("SELECT * from administrador")  
        data = []
        content = {}
        for result in rv:
            content = {'id_adm': result[0], 'rol': result[1]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para agregar un administrador
    def add_administrador(self, rol):
        params = {
            'rol' : rol
        }  
        query = """insert into administrador (rol)
            values (%(rol)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_adm': cursor.lastrowid, 'rol': rol}
        return data
    
    # Funcion para eliminar un administrador
    def delete_administrador(self, id_adm):
        params = {'id_adm' : id_adm}      
        query = """delete from administrador where id_adm = %(id_adm)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = UserModel()     