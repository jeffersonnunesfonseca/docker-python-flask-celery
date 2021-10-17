from .userRepositoryContract import UserRepositoryContract
from uuid import uuid4
from ...controllers import Auth
from api import db

class UserRepositorySQLALCHEMY(db.Model,UserRepositoryContract):
    __tablename__ ="users"
    id=db.Column(db.String(255), primary_key=True)
    nome=db.Column(db.String(200))
    email=db.Column(db.String(200))
    telefone=db.Column(db.String(11))
    telefone2=db.Column(db.String(11))
    nomeEmpresa=db.Column(db.String(200))
    cpfcnpj=db.Column(db.String(18))
    dataNascimento=db.Column(db.String(10))
    sexo=db.Column(db.Enum("M,F"))
    senha=db.Column(db.String(200))

    mockUserList= []    

    def __init__(self) -> None:
        super().__init__()

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