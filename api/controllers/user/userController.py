from .userService import UserService
class UserController:
    
    def __init__(self):
        pass

    def createUser(self,attributes):
        schema = UserService().createUser(attributes)
        return schema.__dict__
