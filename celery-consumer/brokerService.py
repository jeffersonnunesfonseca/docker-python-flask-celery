from celery import Celery
app = Celery('tasks', broker='pyamqp://guest@192.168.15.10/')

@app.task
def add():  
    return "olaaa"