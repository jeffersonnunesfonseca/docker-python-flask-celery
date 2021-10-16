from .userRepository import UserRepository
class UserRepositoryMemory(UserRepository):
    mockUserList= []

    def getById(self,id):
        pass
    
    def getList(self):
        return self.mockUserList

    def create(self,object):
        self.mockUserList.append(object.__dict__)