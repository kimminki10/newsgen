import os
from celery import Celery

from celery.schedules import crontab


# Django 설정 모듈을 Celery 기본값으로 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trandlator.settings')

app = Celery('trandlator')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run-every-20min': {
        'task': 'trandlator.tasks.periodic_task',
        'schedule': crontab(minute='*/20'),
    },
}