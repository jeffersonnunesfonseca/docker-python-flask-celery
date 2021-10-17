from .userRepository import UserRepository
from uuid import uuid4
from ...controllers import Auth
class UserRepositoryMemory(UserRepository):
    mockUserList= []

    def getById(self,id):
        pass
    
    def getList(self):
        return self.mockUserList

    def create(self,object):
        if object.id == None:
            object.id = uuid4()
        
        if hasattr(object, 'senha'):
            object.senha = Auth().generatePassword(object.senha)

        self.mockUserList.append(object.__dict__)
    
    def save(self, object):
        pass
