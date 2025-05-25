# celery_worker.py
from celery import Celery

def make_celery(app_name=_name_):
    return Celery(
        app_name,
        broker='redis://localhost:6379/0',  # Redis URL
        backend='redis://localhost:6379/0'
    )

celery = make_celery()