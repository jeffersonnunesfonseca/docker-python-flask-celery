from celery import Celery
app = Celery(broker='pyamqp://guest@192.168.15.10/')

# @app.tasks("post-form")
@app.task(name="post-form",bind=True)
def teste(self,a):
    print (self.request.id)
    return self.request.id