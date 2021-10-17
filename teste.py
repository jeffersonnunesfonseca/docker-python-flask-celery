from api.models import User
from api.repositories import UserRepositorySQLALCHEMY
from api.controllers import Auth
from pprint import pprint
import hashlib
import os
from sqlalchemy import inspect

def testPassword():
    currentPassword = hashlib.sha256(("teste123"+os.environ.get("SALT_ENCRYPT")).encode()).hexdigest()
    auth = Auth()
    password = "teste123"
    validate = auth.validatePassword(password,currentPassword)

    print(f"current: {len(currentPassword)}\npassword: {len(password)}\nisEqual: {validate}")

def testUserRepository():
    teste = User()
    teste.id=None
    teste.cpfcnpj="421.920.908-54"
    teste.dataNascimento="12/06/1995"
    teste.email="jose@gmail.com"
    teste.nome="jose"
    teste.sexo="M"
    teste.telefone="(41) 99741-9555"
    teste.telefone2="(41) 99943-9555"
    teste.nomeEmpresa="It braba"
    teste.senha="teste123"
    userRepository = UserRepositorySQLALCHEMY(teste)
    userRepository.create()
    userRepository.save()
    objectUserList=userRepository.getList()
    # objectUser=teste.getById("2")
    pprint(objectUserList)

if __name__ == "__main__":
    testUserRepository()
