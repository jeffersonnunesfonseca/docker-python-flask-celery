import multiprocessing
import os
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count()
worker_class = 'eventlet'
timeout = 120 #seconds
loglevel = 'info'
