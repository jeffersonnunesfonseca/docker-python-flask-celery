from abc import ABC, abstractmethod
class UserRepository(ABC):

    @abstractmethod
    def getById(self,id):
        pass
    
    @abstractmethod
    def getList():
        pass

    @abstractmethod
    def create(self,object):
        pass        
