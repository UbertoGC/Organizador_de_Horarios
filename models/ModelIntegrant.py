from connectionPool.pool import MySQLPool

class IntegrantModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_horary_relacionated(self, email):
        params = {'userfk': email}
        rv = self.mysql_pool.execute(
            "SELECT horaryfk from integrant where userfk=%(userfk)s", params)
        array = []
        for result in rv:
            array.append(result[0])
        return array

if __name__ == "__main__":    
    tm = IntegrantModel()     