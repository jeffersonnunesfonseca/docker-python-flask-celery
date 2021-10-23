from celery import Celery
app = Celery(broker='pyamqp://guest@192.168.15.10/')
import sys
sys.path.insert(0,"/home/jeff/Documents/projetosIt/docker-python-flask/")
from api.controllers.user.userController import UserController

# @app.tasks("post-form")
@app.task(name="post-form",bind=True)
def teste(self,attrs):
    user= UserController().createUser(attrs)
    return user

