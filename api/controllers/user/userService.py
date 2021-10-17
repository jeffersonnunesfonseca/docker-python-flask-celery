class UserService:
    
    def __init__(self) -> None:
        pass
    
    def createUser(self,attr):
        if not self.validateTypePayload(type(attr)):
            return False

        for value in attr.keys():
            if not attr[value]:
                return False

        return True
    
    def validateTypePayload(self,type):
        return type == dict