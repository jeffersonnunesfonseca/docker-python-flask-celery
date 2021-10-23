from .userService import UserService
class UserController:
    
    def __init__(self):
        pass

    def sendUserToQueue(self,attributes):
        schema = UserService().createUser(attributes)
        return schema.__dict__

    def createUser(self,attributes):
        schema = UserService().createUser(attributes,True)
        return schema
