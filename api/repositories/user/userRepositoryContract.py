from abc import ABC, abstractmethod,abstractproperty
class UserRepositoryContract:
    
    @abstractproperty
    def id(self):
        return False

    @abstractproperty
    def nome():
        return ""

    @abstractproperty
    def email():
        return ""

    @abstractproperty
    def telefone():
        return ""

    @abstractproperty
    def telefone2():
        return ""

    @abstractproperty
    def nomeEmpresa():
        return ""

    @abstractproperty
    def cpfcnpj():
        return ""

    @abstractproperty
    def dataNascimento():
        return ""

    @abstractproperty
    def sexo():
        return ""

    @abstractproperty
    def senha():
        return ""    
    
    @abstractmethod
    def getById(self,id):
        pass
    
    @abstractmethod
    def getList():
        pass

    @abstractmethod
    def create(self,object):
        pass        
    
    @abstractmethod
    def save(self,object):
        pass        