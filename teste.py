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

def testInsertUserRepository():
    user = User()
    user.id = None
    user.nome = "Jefferson Nunes"
    user.email = "jeff@gmail.com"
    user.telefone = "(41) 99743-9582"
    user.telefone2 = "(41) 88742-5585"
    user.nome_empresa = "It Braba"
    user.cpf_cnpj = "10.495.188/0001-40"
    user.data_nascimento = "1995-06-12"
    user.sexo ="M"
    user.senha ="teste123"
    user.login="jefoffnsffdecdffdfdsdsds"
    userRepository=UserRepositorySQLALCHEMY(user)
    id = userRepository.save()

    if id==None:
        print("Conta ja existe")
    else:
        pprint(id)

def testUserRepository():
    teste = User()
    teste.id=None
    teste.email="jose@gmail.com"
    teste.nome="aaa"
    teste.nome_empresa="Isasaast"
    userRepository = UserRepositorySQLALCHEMY(teste)
    userRepository.update(teste)

if __name__ == "__main__":
    testInsertUserRepository()
