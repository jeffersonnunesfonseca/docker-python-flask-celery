from flask import session,request,url_for,jsonify
from api import app
from .controllers import Auth

@app.route("/")
def index():
    return "Olá mundo"

@app.route("/generateToken/")
def generateToken():  
    try:
        token = Auth()
        return token.generateToken(request.json)
    except:
        return jsonify({"error": "bad request"}), 400

@app.route("/decodeToken",methods=['POST'])
def decodeToken():  
    try:
        token = Auth()
        print(request.json)
        return token.decodeJwt(request.json["token"])
    except:
        return jsonify({"error": "bad request"}), 400

@app.route('/<path:text>', methods=['GET', 'POST'])
def all_routes(text):
    return jsonify({"error": "bad reques2t"}), 400