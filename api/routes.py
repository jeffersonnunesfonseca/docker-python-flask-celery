from flask import session,request,url_for,jsonify
from api import app
from api.controllers.auth.jwt import Jwt

@app.route("/")
def index():
    return "Olá mundo"

@app.route("/generateToken/")
def generateToken():  
    try:
        jwt = Jwt()
        return jwt.generateToken(request.json)
    except:
        return jsonify({"error": "bad request"}), 400

@app.route("/decodeToken",methods=['POST'])
def decodeToken():  
    try:
        jwt = Jwt()
        print(request.json)
        return jwt.decodeJwt(request.json["token"])
    except:
        return jsonify({"error": "bad request"}), 400

@app.route('/<path:text>', methods=['GET', 'POST'])
def all_routes(text):
    return jsonify({"error": "bad reques2t"}), 400