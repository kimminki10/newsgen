import os
import pytz
import threading
from django.apps import AppConfig
from django.conf import settings

from .jobs_status import is_job_registered, register_job,clear_job_status,job_id  # 작업 상태 관리 함수 가져오기

import atexit

def scheduled_ticker():
    from .jobs import Automate_Tickers
    print("--scheduled_Automate_Tickers--")
    Automate_Tickers()

def scheduled_automate():
    from .jobs import Automate
    print("--scheduled_automate--")
    Automate()
    
scheduled_task = None

class TrandlatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trandlator'
    global job_id
    def ready(self):
        if is_job_registered(job_id):
            return
        # 중복 실행 방지 (디버그 모드시 두번 실행됨)
        if os.environ.get('RUN_MAIN') != 'true':
            print("Skipping duplicate scheduler initialization")
            return
        print("Scheduler ready")
       
        if settings.DEBUG:
            print("Scheduler ready debug")
            # 스케줄러 초기화를 별도의 스레드에서 수행
            
            scheduled_task = threading.Thread(target=self.start_scheduler)
            scheduled_task.start()

    def start_scheduler(self):
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.executors.pool import ThreadPoolExecutor
        from apscheduler.triggers.interval import IntervalTrigger
        from django_apscheduler.jobstores import DjangoJobStore, register_events
        from apscheduler.triggers.cron import CronTrigger
        from crawling.services.set_tickers import add_new_tickers

        if is_job_registered(job_id):
            print("Job already registered. Skipping registration.")
            return
        register_job(job_id)

        #서버 실행시 초기 tickers 등록
        add_new_tickers()
        print("Registering new job...")

        kst = pytz.timezone('Asia/Seoul')
        # (실행할 함수, 타이머, 서버 실행시 즉시 실행 한번 할지 여부 )
        schedulerFuncs =[
            (scheduled_ticker,CronTrigger(hour=23, minute=30, timezone=kst),True), #미국장 시작 11:30  pm (한국시간)
            (scheduled_automate,IntervalTrigger(minutes=1),True)
        ]

        

        
        for func,trigger,isImmediately in schedulerFuncs:
            scheduler = BackgroundScheduler(
                jobstores={
                    'default': DjangoJobStore(),
                },
                executors={
                    'default': ThreadPoolExecutor(20),
                },
                job_defaults={
                    'coalesce': False,
                    'max_instances': 1,
                },
            )

            # 종료 시 스케줄러를 중지하도록 설정
            atexit.register(self.shutdown_scheduler, scheduler)

            register_events(scheduler)
            scheduler.start()
            print(f"Scheduler register : {func.__name__}")
            # 1분마다 실행되는 작업 등록
            scheduler.add_job(
                func,
                trigger,
                id=func.__name__,
                replace_existing=False
            )
            if isImmediately == True:
                func()

    def shutdown_scheduler(self, scheduler):
        """스케줄러를 안전하게 종료"""
        clear_job_status()
        print(f"스케줄러 종료 중 (잠시만 기다려주세요)...")

        for job in scheduler.get_jobs():
            scheduler.remove_job(job.id)

        scheduler.shutdown(wait=False)  # 스케줄러 중지

