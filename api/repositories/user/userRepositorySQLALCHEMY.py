from .userRepositoryContract import UserRepositoryContract
from uuid import uuid4
from ...controllers import Auth
from ...models import User
from api import db
from sqlalchemy import insert
class UserRepositorySQLALCHEMY(db.Model,UserRepositoryContract):
    """
    setando atributos no repository mesmo que ja esteja setado na model, isso por que não quero gerar que minha model 
    fique dependendo do db para dizer as tipagens,estou uma melhor forma.
    """ 
    __tablename__ ="users"
    id=db.Column(db.String(255), primary_key=True)
    nome=db.Column(db.String(200))
    email=db.Column(db.String(200))
    telefone=db.Column(db.String(16))
    telefone2=db.Column(db.String(16))
    nomeEmpresa=db.Column(db.String(200))
    cpfcnpj=db.Column(db.String(18))
    dataNascimento=db.Column(db.String(10))
    sexo=db.Column(db.Enum("M","F"))
    senha=db.Column(db.String(200))
    
    def __init__(self,object:User) -> None:
        values = object.__dict__  
        self.id = values["id"]
        self.nome = values["nome"]
        self.email = values["email"]
        self.telefone = values["telefone"]
        self.telefone2 = values["telefone2"]
        self.nomeEmpresa = values["nomeEmpresa"]
        self.cpfcnpj = values["cpfcnpj"]
        self.dataNascimento = values["dataNascimento"]
        self.sexo = values["sexo"]
        self.senha = values["senha"]
        

    def getById(self,id):
        return self.query.get(id)
    
    def getList(self):
        return self.__dict__

    def create(self):
        if self.id == None:
            self.id = uuid4()
        
        if hasattr(self, 'senha'):
            self.senha = Auth().generatePassword(self.senha)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        # insert("users").values(self)