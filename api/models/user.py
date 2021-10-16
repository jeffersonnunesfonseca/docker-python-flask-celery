from ..repositories import UserRepositoryMemory
class User(UserRepositoryMemory) :
    id=None
    nome=""
    idade=0

    def __init__(self,id,nome,idade):
        self.id = id
        self.nome=nome
        self.idade=idade

        super().create(self)
        lista = super().getList()

        print(lista)

