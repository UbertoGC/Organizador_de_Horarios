from models.ModelHour import HourModel
import datetime
class HourController:
    def __init__(self):        
        self.hourmodel = HourModel()
    
    def create_hour(self, title, description, start_date, final_date, horary_id):
        primerafecha = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M")
        ultimafecha = datetime.datetime.strptime(final_date, "%Y-%m-%d %H:%M")
        diferencia = ultimafecha - primerafecha
        if(diferencia.total_seconds() < 0):
            return "La fecha de inicio es mayor que la fecha de finalización", "Error"
        elif(diferencia.total_seconds() > 86400):
            return "Los eventos no pueden durar más de 24 horas", "Error"
        params = {'title': title, 'description': description, 'startDate': start_date, 'finalDate': final_date, 'horaryfk': horary_id}
        self.hourmodel.create_hour(params)
        return "Hora agregada con exito", "Logrado"

    def eliminate_hour(self, id):
        self.hourmodel.eliminate_hour(id)

if __name__ == "__main__":    
    tm = HourController()    