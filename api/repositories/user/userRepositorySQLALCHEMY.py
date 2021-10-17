from sqlalchemy.orm import session
from .userRepositoryContract import UserRepositoryContract
from uuid import uuid4
from ...controllers import Auth
from ...models import User
from api import db
import datetime
from sqlalchemy import update
class UserRepositorySQLALCHEMY(db.Model,UserRepositoryContract):

    __tablename__ ="users"
    id=db.Column(db.String(255), primary_key=True)
    nome=db.Column(db.String(200))
    email=db.Column(db.String(200))
    nome_empresa=db.Column(db.String(200))
    telefone=db.Column(db.String(16))
    telefone2=db.Column(db.String(16))
    cpf_cnpj=db.Column(db.String(18))
    data_nascimento=db.Column(db.DateTime)
    sexo=db.Column(db.Enum("F","M"))
    login=db.Column(db.String(45))
    senha=db.Column(db.String(255))
    created_at=db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at=db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    deleted=db.Column(db.Integer(),default=0)

    def __init__(self,user:User) -> None:
        self.id = user.id
        self.nome = user.nome
        self.email = user.email
        self.telefone = user.telefone
        self.telefone2 = user.telefone2
        self.nome_empresa = user.nome_empresa
        self.cpf_cnpj = user.cpf_cnpj
        self.data_nascimento =user.data_nascimento
        self.sexo =user.sexo
        self.senha =user.senha
        self.login=user.login
        self.deleted=user.deleted
       
    def getById(self,id):
        return self.query.get(id)
    
    def getList(self):
        return self.__dict__
    
    def updateById(self,field,value):
        result = db.session.query(UserRepositorySQLALCHEMY).filter(UserRepositorySQLALCHEMY.id == self.id).one()
        setattr(result,field,value)
        db.session.commit()

    def create(self):
        if self.id == None:
            self.id = uuid4()
        
        if hasattr(self, 'senha'):
            self.senha = Auth().generatePassword(self.senha)
    
    def save(self):
        db.session.add(self)
        db.session.commit()