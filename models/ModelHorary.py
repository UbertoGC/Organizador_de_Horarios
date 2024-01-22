from connectionPool.pool import MySQLPool

class HoraryModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def create_horary(self, params):
        query_1 = """INSERT INTO horary (title, description, userfk)
            values (%(title)s, %(description)s, %(userfk)s)"""
        query_2 = """SELECT id FROM horary WHERE userfk=%(userfk)s 
            AND title=%(title)s AND description=%(description)s"""
        self.mysql_pool.execute(query_1, params, commit=True)
        rv = self.mysql_pool.execute(query_2,params)
        for result in rv:
            id_horary = result[0]
            return id_horary

    def get_autor(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute(
            "SELECT userfk from horary where id=%(id)s", params)
        content = {}
        for result in rv:
            content = {
                'autor': result[0]}
            return content

    def get_horary_created(self, email):
        params = {'userfk': email}
        rv = self.mysql_pool.execute(
            "SELECT title, description, userfk from horary where userfk=%(email)s", params)
        content = {}
        array = []
        for result in rv:
            content = {
                'title': result[0], 'description': result[1], 'autor': result[2]}
            array.append(content)
        return array
    
    def get_horary_by_id(self, list_id):
        array = []
        if(len(list_id) == 0):
            return array
        consult = "SELECT id, title, description, userfk from horary where id="
        for i in range(len(list_id)):
            consult = consult + str(list_id[i])
            if(i < (len(list_id)-1)):
                consult = consult + " OR id="
        rv = self.mysql_pool.execute(consult)
        content = {}
        
        for result in rv:
            content = {
                'id': result[0], 'title': result[1], 'description': result[2], 'autor': result[3]}
            array.append(content)
        return array

    def get_horary_by_conditions(self, list_id, title, autor):
        consult = "SELECT id, title, description, userfk from horary WHERE ("
        for i in range(len(list_id)):
            consult  += "id=" + str(list_id[i])
            if(i < (len(list_id)-1)):
                consult += " OR "
        consult += ")"
        if(title != ''):
            consult += " AND title='" + title + "'"
        if(autor != ''):
            consult += " AND userfk='" + autor + "'"
        
        rv = self.mysql_pool.execute(consult)
        content = {}
        array = []
        for result in rv:
            content = {
               'id': result[0], 'title': result[1], 'description': result[2], 'autor': result[3]}
            array.append(content)
        return array
    
    def get_integrants(self, horary_id):
        params = {"horary_id": horary_id}
        query = "SELECT * FROM integrant WHERE horaryfk = %(horary_id)s"
        rv = self.mysql_pool.execute(query, params)
        content = {}
        array = []
        for result in rv:
            content = {
               'userfk': result[0], 'description': result[1], 'horaryfk': result[2] 
            }
            array.append(content)
        return array

    def get_hours_by_horary_id(self, horary_id):
        params = {"horary_id": horary_id}
        query = "SELECT * FROM hour WHERE horaryfk = %(horary_id)s"
        rv = self.mysql_pool.execute(query, params)
        content = {}
        array = []
        for result in rv:
            content = {
               'id': result[0], 'startDate': str(result[1]).split(' ')[0], 'startTime': str(result[1]).split(' ')[1], 'finalDate': str(result[2]).split(' ')[0], 'finalTime': str(result[2]).split(' ')[1], 'title': result[3]}
            array.append(content)
        return array

if __name__ == "__main__":    
    tm = HoraryModel()     