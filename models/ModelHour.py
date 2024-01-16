from connectionPool.pool import MySQLPool

class HourModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def create_hour(self, params):
        query = """INSERT INTO hour (title, description, startDate, finalDate, horaryfk)
            values (%(title)s, %(description)s, %(startDate)s, %(finalDate)s, %(horaryfk)s)"""
    
        cursor = self.mysql_pool.execute(query, params, commit=True)
        return cursor

if __name__ == "__main__":    
    tm = HourModel()
