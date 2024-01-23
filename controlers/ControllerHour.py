from models.ModelHour import HourModel

class HourController:
    def __init__(self):        
        self.hourmodel = HourModel()
    
    def create_hour(self, title, description, start_date, final_date, horary_id):
        print(" aaaaaaaaaaa 1")
        params = {'title': title, 'description': description, 'startDate': start_date, 'finalDate': final_date, 'horaryfk': horary_id}
        cursor = self.hourmodel.create_hour(params)
        return cursor

if __name__ == "__main__":    
    tm = HourController()    