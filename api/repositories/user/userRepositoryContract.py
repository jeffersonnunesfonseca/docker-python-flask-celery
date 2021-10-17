from abc import ABC, abstractmethod,abstractproperty
class UserRepositoryContract:
    @abstractmethod
    def getById(self,id):
        pass
    
    @abstractmethod
    def getList():
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def create(self):
        pass        
    
    @abstractmethod
    def save(self):
        pass        