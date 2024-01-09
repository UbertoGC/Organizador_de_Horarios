from connectionPool.pool import MySQLPool

class IntegrantModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def add_integrant(self, userfk, horaryfk):
        params = {'userfk':userfk, 'horaryfk':horaryfk}
        self.mysql_pool.execute("INSERT INTO integrant (userfk, horaryfk) values (%(userfk)s, %(horaryfk)s)", params, commit=True)

    def get_horary_relacionated(self, email):
        params = {'userfk': email}
        rv = self.mysql_pool.execute(
            "SELECT horaryfk from integrant where userfk=%(userfk)s", params)
        array = []
        for result in rv:
            array.append(result[0])
        return array
    
    def get_horary_relacionated_various(self, username, emails):
        consult = "SELECT inte1.horaryfk from integrant inte1 INNER JOIN integrant inte2 "
        consult += "ON inte1.horaryfk = inte2.horaryfk where inte1.userfk = "
        consult += ("'" + username + "' AND (")
        for i in range(len(emails)):
            consult += ("inte2.userfk = '" + emails[i] + "'")
            if(i < (len(emails)-1)):
                consult += " OR "
        consult = consult + ") GROUP BY inte1.horaryfk"
        rv = self.mysql_pool.execute(consult)
        array = []
        for result in rv:
            array.append(result[0])
        return array
    
if __name__ == "__main__":    
    tm = IntegrantModel()     