from ..repositories import UserRepositoryMemory
class User(UserRepositoryMemory) :
    id=None
    nome=""
    email=""
    telefone=""
    telefone2=""
    nomeEmpresa=""
    cpfcnpj=""
    dataNascimento=""
    sexo=""
    senha=""