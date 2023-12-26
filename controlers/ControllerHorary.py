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
            horarios.remove(6)
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

if __name__ == "__main__":    
    tm = HoraryController()    