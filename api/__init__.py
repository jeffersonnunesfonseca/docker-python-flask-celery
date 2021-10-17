# from flask import Flask
# import os
# from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import pymysql
pymysql.install_as_MySQLdb()

# app = Flask(__name__)
# app.url_map.strict_slashes = False # ignora se termina ou nao com barra

# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
# # app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("SQLALCHEMY_DATABASE_URI")
# app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:12345@192.168.15.10:3306/webserver"
# db = SQLAlchemy(app)

# from api import routes
# db.create_all()
# db.session.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:12345@192.168.15.10:3306/webserver"
db = SQLAlchemy(app)
from api.models import User

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username
