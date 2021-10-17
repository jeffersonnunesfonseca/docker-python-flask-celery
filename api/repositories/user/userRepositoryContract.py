from abc import ABC, abstractmethod,abstractproperty
class UserRepositoryContract:
    @abstractmethod
    def getById(self,id):
        pass
    
    @abstractmethod
    def getList():
        pass

    @abstractmethod
    def update(self,object):
        pass
    
    @abstractmethod
    def save(self):
        pass        