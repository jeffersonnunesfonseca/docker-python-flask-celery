from celery import Celery
appCelery=Celery(broker="pyamqp://guest@localhost//",)
