from connectionPool.pool import MySQLPool
import datetime

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
    
    def diference_between_hours(self, first_hour, second_hour):
        diference = first_hour - second_hour
        minutos = int(diference.total_seconds()/60)
        return minutos

    def arreglar_fechas(self, content, fecha_inicial, fecha_final, primer_dia, ultimo_dia):
        fecha_primera = datetime.datetime.strptime((str(primer_dia) + ' 00:00:00'), "%Y-%m-%d %H:%M:%S")
        fecha_ultima = datetime.datetime.strptime((str(ultimo_dia) + ' 00:00:00'), "%Y-%m-%d %H:%M:%S")
        if(fecha_primera.date() > fecha_inicial.date()):
            fecha_inicial = fecha_primera
        if(fecha_ultima.date() < fecha_final.date()):
            fecha_final = fecha_ultima
        content['duracion_minutos'] = self.diference_between_hours(fecha_final, fecha_inicial)
        content['dia_inicial'] = fecha_inicial.weekday()
        content['hora_inicial'] = fecha_inicial.hour
        content['minuto_inicial'] = fecha_inicial.hour * 60 + fecha_inicial.minute
        return content

    def get_hours_by_range(self, horary_id, primer_dia, ultimo_dia):
        params = {"horary_id": horary_id, "first_day": str(primer_dia) + ' 00:00:00', "last_day":str(ultimo_dia) + ' 00:00:00'}
        query = "SELECT * FROM hour WHERE horaryfk = %(horary_id)s AND ((startDate >= %(first_day)s AND startDate < %(last_day)s)"
        query = query + " OR (finalDate > %(first_day)s AND finalDate < %(last_day)s)) order by startDate"
        rv = self.mysql_pool.execute(query, params)
        content = {}
        array = []
        for result in rv:
            content = {
               'id': result[0],
               'startDate': datetime.datetime.strptime(str(result[1]), "%Y-%m-%d %H:%M:%S"),
               'finalDate': datetime.datetime.strptime(str(result[2]), "%Y-%m-%d %H:%M:%S"),
               'tittle': result[3],
               'description': result[4]
            }
            fecha_inicial = content['startDate']
            fecha_final = content['finalDate']
            if(fecha_inicial.date() != fecha_final.date()):
                new_content_1 = content.copy()
                new_content_2 = content.copy()
                fecha_index = fecha_inicial + datetime.timedelta(days=1, hours= -fecha_inicial.hour, minutes= -fecha_inicial.minute, seconds= -fecha_inicial.second)                
                if(fecha_inicial.date() >= primer_dia):
                    new_content_1 = self.arreglar_fechas(new_content_1,fecha_inicial,fecha_index,primer_dia,ultimo_dia)
                    array.append(new_content_1)
                if(fecha_index.date() != ultimo_dia):                    
                    new_content_2 = self.arreglar_fechas(new_content_2,fecha_index,fecha_final,primer_dia,ultimo_dia)
                    array.append(new_content_2)
            else:
                new_content = self.arreglar_fechas(content, fecha_inicial, fecha_final,primer_dia, ultimo_dia)
                array.append(new_content)

        return array
    def eliminate_horary(self, id):
        query_1 = "DELETE from integrant WHERE horaryfk = "+id
        query_2 = "DELETE from hour WHERE horaryfk = "+id
        query_3 = "DELETE from horary WHERE id = "+id
        self.mysql_pool.execute(query_1,None,commit=True)
        self.mysql_pool.execute(query_2,None,commit=True)
        self.mysql_pool.execute(query_3,None,commit=True)

if __name__ == "__main__":    
    tm = HoraryModel()     