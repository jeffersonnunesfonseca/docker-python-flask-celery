import sys
sys.path.insert(0,"/usr/src/app")
from api.controllers.user.userService import UserService
import unittest
class UserServiceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dictMock= {
            "nome": "a",
            "email": "a",
            "telefone": "a",
            "telefone2": "a",
            "nome_empresa": "a",
            "cpf_cnpj": "a",
            "data_nascimento": "1995-06-12",
            "sexo": "M",
            "senha": "a",
            "login": "a"
        }   
        cls.dictMock=dictMock

    @classmethod
    def tearDownClass(cls):
        cls.dictMock=None

    def test_payload_is_dict(self):
        self.assertTrue(UserService().validateTypePayload(type(self.dictMock)),"payload deve ser um json")

    def test_validate_payload(self):
        self.assertTrue(UserService().createUser(self.dictMock),"payload nao pode ter campo vazio")