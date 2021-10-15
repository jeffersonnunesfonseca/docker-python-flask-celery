import jwt
import os
class Jwt :
    
    def __init__(self):
        pass

    def generateToken(self,payload):
        return {"token":jwt.encode(payload, os.environ.get('SECRET_JWT'), algorithm="HS256")}
    
    def decodeJwt(self,hash):
        return jwt.decode(hash, os.environ.get('SECRET_JWT'), algorithms=["HS256"])