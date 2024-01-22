from models.ModelIntegrant import IntegrantModel
class IntegrantController:
    def __init__(self):        
        self.integrantmodel = IntegrantModel()
        
    def add_integrant(self, userfk, horaryfk):
        self.integrantmodel.add_integrant(userfk, horaryfk)

if __name__ == "__main__":    
    tm = IntegrantController()    