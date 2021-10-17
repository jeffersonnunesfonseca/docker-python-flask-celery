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
    teste.id="21069a0c-6d26-4959-9f4c-add47d74650a"
    teste.cpf_cnpj="421.920.908-54"
    teste.data_nascimento="1995-06-12"
    teste.email="jose@gmail.com"
    teste.nome="aaa"
    teste.sexo="M"
    teste.telefone="(41) 99741-9555"
    teste.telefone2="(41) 99943-9555"
    teste.nome_empresa="It braba"
    teste.senha="teste123"
    # pprint(teste.__dict__)
    userRepository = UserRepositorySQLALCHEMY(teste)
    # userRepository.create()
    # userRepository.save()

    userRepository.updateById("nome","zicudo")

    # objectUserList=userRepository.getList()
    # objectUser=teste.getById("2")
    # pprint(objectUserList)

if __name__ == "__main__":
    testUserRepository()
