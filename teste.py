from api.controllers.auth.jwt import Jwt

jwt = Jwt()

payload = {"nome": "jeff", "age":25}
token = jwt.generateToken(payload)
print("Token: ",format(token))

decodedToken = jwt.decodeJwt(token)
print("Token decoded: ",format(decodedToken))

print(decodedToken["age"])
