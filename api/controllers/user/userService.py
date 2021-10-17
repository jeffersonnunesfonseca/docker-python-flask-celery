from ...repositories import UserRepositorySQLALCHEMY
from ...models import User

class UserService:
    
    def __init__(self) -> None:
        pass
    
    def createUser(self,attr):
        if not self.validateTypePayload(type(attr)):
            return False

        for value in attr.keys():
            if not attr[value]:
                return False

        user = User()
        user.nome = attr["nome"]
        user.email = attr["email"]
        user.telefone = attr["telefone"]
        user.telefone2 = attr["telefone2"]
        user.nome_empresa = attr["nome_empresa"]
        user.cpf_cnpj = attr["cpf_cnpj"]
        user.data_nascimento = attr["data_nascimento"]
        user.sexo = attr["sexo"]
        user.senha = attr["senha"]
        user.login=attr["login"]
        result = UserRepositorySQLALCHEMY(user).save()
        print(result)
        return result
    
    def validateTypePayload(self,type):
        return type == dict