from connectionPool.pool import MySQLPool

class HoraryModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_horary_created(self, email):
        params = {'userfk': email}
        rv = self.mysql_pool.execute(
            "SELECT title, description, userfk from horary where email=%(email)s", params)
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

if __name__ == "__main__":    
    tm = HoraryModel()     