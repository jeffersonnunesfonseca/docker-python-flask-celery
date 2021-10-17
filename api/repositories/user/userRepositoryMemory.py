from .userRepositoryContract import UserRepositoryContract
from uuid import uuid4
from ...controllers import Auth
class UserRepositoryMemory(UserRepositoryContract):
    id=None
    nome=""
    email=""
    telefone=""
    telefone2=""
    nomeEmpresa=""
    cpfcnpj=""
    dataNascimento=""
    sexo=""
    senha=""   
    mockUserList= []    
    
    def getById(self,id):
        for object in self.mockUserList:
            if object["id"] == id:
                return object
        return f"value not found by id {id}"
    
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
