from django.apps import AppConfig
from django.conf import settings
from .jobs_status import is_job_registered, register_job  # 작업 상태 관리 함수 가져오기
import threading
import os


class TrandlatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trandlator'

    def ready(self):
         # 중복 실행 방지 (디버그 모드시 두번 실행됨)
        if os.environ.get('RUN_MAIN') != 'true':
            print("Skipping duplicate scheduler initialization")
            return
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

        #Automate()

       
       
        job_id = "automate_job"  # 작업의 고유 ID
        if not is_job_registered(job_id):
            register_job(job_id)
            print("Registering new job...")
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

            Automate()
            
            # Register the job
            @register_job(scheduler, IntervalTrigger(seconds=10), id=job_id, replace_existing=False)
            def scheduled_automate():
                Automate()
        else:
            print("Job already registered. Skipping registration.")