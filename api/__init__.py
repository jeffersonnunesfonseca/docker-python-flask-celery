import os
import mysql.connector
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:12345@192.168.15.10:3306/webserver"
db = SQLAlchemy(app)
from api import routes