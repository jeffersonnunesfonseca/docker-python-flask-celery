import jwt
import os
import hashlib
class Auth :
    
    def __init__(self):
        pass

    def generateToken(self,payload):
        return {"token":jwt.encode(payload, os.environ.get('SECRET_JWT'), algorithm="HS256")}
    
    def decodeJwt(self,hash):
        return jwt.decode(hash, os.environ.get('SECRET_JWT'), algorithms=["HS256"])

    def generatePassword(self,password):
        return hashlib.sha256((password+os.environ.get("SALT_ENCRYPT")).encode()).hexdigest()

    def validatePassword(self,password,currentPassword):
        return self.generatePassword(password) == currentPassword
