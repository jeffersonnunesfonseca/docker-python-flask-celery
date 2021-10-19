from celery import Celery
app=Celery(broker="pyamqp://guest@localhost//",)

@app.task
def sendToBroker():
    return "ola mundo"

    