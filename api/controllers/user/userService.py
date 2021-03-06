from ...repositories import UserRepositorySQLALCHEMY
from ...models import User
from ...controllers.broker.brokerService import BrokerService

class UserService:
    
    def __init__(self) -> None:
        pass
    
    def createUser(self,attr,saveBd=False):

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
        if(saveBd ==True):
            return UserRepositorySQLALCHEMY(user).save()
        else:
            BrokerService.customerForm(user.__dict__)
            return {
                "msg":"sended to queue"
            }
    
    def validateTypePayload(self,type):
        return type == dict
    