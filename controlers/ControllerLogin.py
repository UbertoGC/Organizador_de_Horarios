from models.ModelUser import UserModel
class LoginController:
    def __init__(self):        
        self.usermodel = UserModel()

    def iniciate_session(self, email, password):
        user = self.usermodel.get_user_username(email)
        if(user == None):
            return 0
        elif (user['password'] == password):
            return 1
        else:
            return 2
        
    def add_user(self, data):
        cursor = self.usermodel.add_user(data)
        return cursor


if __name__ == "__main__":    
    tm = LoginController()    