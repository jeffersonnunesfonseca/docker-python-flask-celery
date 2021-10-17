from ..repositories import UserRepositoryMemory
from ..repositories import UserRepositorySQLALCHEMY
class User(UserRepositorySQLALCHEMY):
    def __init__(self) -> None:
        # super().__init__(self)
        pass


    def getCustomList(self):
        return self.query.all() 


