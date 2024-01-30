from models.ModelHorary import HoraryModel
from models.ModelIntegrant import IntegrantModel
import datetime

class HoraryController:
    def __init__(self):        
        self.horarymodel = HoraryModel()
        self.integrantmodel = IntegrantModel()

    def horary_relationed(self, email):
        array = self.integrantmodel.get_horary_relacionated(email)
        horarios = self.horarymodel.get_horary_by_id(array)
        while len(horarios) > 6:
            horarios.remove(horarios[6])
        return horarios

    def horary_filtrated(self, email, title, autor, integrants):
        array = []
        horarios = []
        if(len(integrants) > 0):
            array = self.integrantmodel.get_horary_relacionated_various(email,integrants)
        else:
            array = self.integrantmodel.get_horary_relacionated(email)

        if(len(array) > 0):
            horarios = self.horarymodel.get_horary_by_conditions(array,title,autor)
        return horarios
    
    def create_horary(self,email, title, description):
        params = {'title': title, 'description': description, 'userfk': email}
        id_horary = self.horarymodel.create_horary(params)
        self.integrantmodel.add_integrant(email, id_horary)

    def get_integrants(self, horary_id):
        integrantes = self.horarymodel.get_integrants(horary_id)
        return integrantes

    def check_autor(self, id, username):
        resultados = self.horarymodel.get_autor(id)
        if( username != resultados['autor']):
            return False
        else:
            return True
    
    def get_hours_by_calendar_mode(self, horary_id, number_of_week):
        dia_actual = datetime.datetime.now().date()
        primer_dia = dia_actual - datetime.timedelta(days=dia_actual.weekday())
        primer_dia = primer_dia + datetime.timedelta(days = (7*number_of_week))
        ultimo_dia = primer_dia + datetime.timedelta(days = 7)
        horarios = self.horarymodel.get_hours_by_range(horary_id,primer_dia, ultimo_dia)

        array = []
        for i in range(24):
            array.append([])
            for j in range(7):
                array[i].append([])
        
        for content in horarios:
            index_h = content['hora_inicial']
            index_d = content['dia_inicial']
            array[index_h][index_d].append(content)

        list_of_days=[]
        for i in range(7):
            dia_i = primer_dia + datetime.timedelta(days = i)
            list_of_days.append(str(dia_i))
        return array, list_of_days, str(primer_dia), str(ultimo_dia + datetime.timedelta(days = -1))
    
    def get_diference_of_date(self, hora):
        dia_buscar = datetime.datetime.strptime(hora,'%Y-%m-%d').date()
        primer_dia_buscar = dia_buscar - datetime.timedelta(days=dia_buscar.weekday())

        dia_actual = datetime.datetime.now().date()
        primer_dia = dia_actual - datetime.timedelta(days=dia_actual.weekday())

        if(primer_dia_buscar == primer_dia):
            return '0'
        else:
            diference = (primer_dia_buscar - primer_dia).days
            diference = int(diference/7)
            return str(diference)
    
    def eliminate_horary(self, id):
        self.horarymodel.eliminate_horary(id)

if __name__ == "__main__":    
    tm = HoraryController()    