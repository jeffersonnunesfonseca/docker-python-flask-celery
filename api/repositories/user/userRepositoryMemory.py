from .userRepository import UserRepository
from uuid import uuid4
class UserRepositoryMemory(UserRepository):
    mockUserList= []

    def getById(self,id):
        pass
    
    def getList(self):
        return self.mockUserList

    def create(self,object):
        if object.id == None:
            object.id = uuid4()
        self.mockUserList.append(object.__dict__)