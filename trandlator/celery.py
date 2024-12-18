from celery import Celery
from celery.schedules import crontab
import os

# Django 프로젝트 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trandlator.settings')

# Celery 앱 생성
app = Celery('trandlator')

# Django 설정과 통합
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()  # tasks 앱 명시

app.conf.beat_schedule = {
    'my_periodic_task': {
        'task': 'tasks.tasks.my_periodic_task',
        'schedule': crontab(minute='*/1'),
    }
}