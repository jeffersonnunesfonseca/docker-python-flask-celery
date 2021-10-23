from flask import session,request,url_for,jsonify
from api import app
from .controllers import AuthController, UserController

@app.route("/")
def index():
    return "Olá mundo"

@app.route("/generateToken/")
def generateToken():  
    try:
        token = AuthController()
        return token.generateToken(request.json)
    except TypeError as e:
        return jsonify({"error": "invalid reuqest"}), 400
    except:
        return jsonify({"error": "bad request"}), 400

@app.route("/decodeToken",methods=['POST'])
def decodeToken():  
    try:
        token = AuthController()
        print(request.json)
        return token.decodeJwt(request.json["token"])
    except:
        return jsonify({"error": "bad request"}), 400

@app.route("/createUser",methods=['POST'])
def createUser():  
    try:
        user = UserController()
        return user.sendUserToQueue(request.json)
    except:
        return jsonify({"error": "bad request"}), 400



@app.route('/<path:text>', methods=['GET', 'POST'])
def all_routes(text):
    return jsonify({"error": "bad reques2t"}), 400
