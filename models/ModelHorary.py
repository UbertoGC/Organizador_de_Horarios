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
        consult = "SELECT id, title, description, userfk from horary where id="
        for i in range(len(list_id)):
            consult = consult + str(list_id[i])
            if(i < (len(list_id)-1)):
                consult = consult + " OR id="
        rv = self.mysql_pool.execute(consult)
        content = {}
        array = []
        for result in rv:
            content = {
                'id': result[0], 'title': result[1], 'description': result[2], 'autor': result[3]}
            array.append(content)
        return array
    
    def organizate_conditions(self, conditions_status, conditions_table):
        conditions = " where "
        if(conditions_status[0]):
            conditions += ("(" + conditions_table[0] + ")")
        if(conditions_status[1]):
            if(conditions_status[0]):
                conditions = conditions + " and "
            conditions += ("(" + conditions_table[1] + ")")
        if(conditions_status[2]):
            if(conditions_status[0] or conditions_status[1]):
                conditions = conditions + " and "
            conditions += ("(" + conditions_table[2] + ")")   
        return conditions

    def get_horary_by_conditions(self, list_id, title, autor):
        consult = "SELECT id, title, description, userfk from horary"
        one_condition = 0
        conditions_status = [False,False,False]
        conditions_table = ["","",""]

        if(len(list_id) > 0):
            for i in range(len(list_id)):
                conditions_table[0]  = conditions_table[0] + "id=" + str(list_id[i])
                if(i < (len(list_id)-1)):
                    conditions_table[0] += " OR "
            one_condition = True
            conditions_status[0] = True
        if(title != ''):
            conditions_table[1] ="title=" + "'" + title + "'"
            one_condition = True
            conditions_status[1] = True
        if(autor != ''):
            conditions_table[2] ="userfk=" + "'" + autor + "'"
            one_condition = True
            conditions_status[2] = True
        if one_condition:
            consult += self.organizate_conditions(conditions_status, conditions_table)

        print(consult)
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