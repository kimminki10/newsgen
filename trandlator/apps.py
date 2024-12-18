from django.apps import AppConfig
from django.conf import settings
import threading

class TrandlatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trandlator'

    def ready(self):
        print("Scheduler ready")
        if settings.DEBUG:
            print("Scheduler ready debug")
            # 스케줄러 초기화를 별도의 스레드에서 수행
            threading.Thread(target=self.start_scheduler).start()

    def start_scheduler(self):
        from .jobs import Automate
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.executors.pool import ThreadPoolExecutor
        from apscheduler.triggers.interval import IntervalTrigger
        from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
        
        Automate()
        
        print("Scheduler started")
        scheduler = BackgroundScheduler({
            'jobstores': {
                'default': DjangoJobStore(),
            },
            'executors': {
                'default': ThreadPoolExecutor(20),
            },
            'job_defaults': {
                'coalesce': False,
                'max_instances': 1,
            },
        })
        register_events(scheduler)
        scheduler.start()

        # Register the job
 
        #@register_job(scheduler, IntervalTrigger(seconds=10))
        @register_job(scheduler, IntervalTrigger(minutes=5))
        def scheduled_Automate():
            Automate()