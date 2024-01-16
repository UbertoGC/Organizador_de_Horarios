from models.ModelHour import HourModel

class HourController:
    def __init__(self):        
        self.horarymodel = HourModel()
    
    def create_hour(self, title, description, start_date, final_date):

        params = {'title': title, 'description': description, 'startDate': start_date, 'finalDate': final_date, 'horaryfk': id}
        cursor = self.horarymodel.create_hour(params)
        return cursor

if __name__ == "__main__":    
    tm = HourController()    