from flask import session,request,url_for
from api import app

@app.route("/")
def index():
    return "Olá mundo"