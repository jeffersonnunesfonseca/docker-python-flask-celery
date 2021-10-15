from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False # ignora se termina ou nao com barra
from api import routes