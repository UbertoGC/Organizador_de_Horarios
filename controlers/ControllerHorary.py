from models.ModelHorary import HoraryModel
from models.ModelIntegrant import IntegrantModel

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

    def get_hours_by_horary_id_controller(self, horary_id):
        horarios = self.horarymodel.get_hours_by_horary_id(horary_id)
        return horarios

if __name__ == "__main__":    
    tm = HoraryController()    