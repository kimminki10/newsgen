import os
import pytz
import threading
from django.apps import AppConfig
from django.conf import settings


from .jobs_status import is_job_registered, register_job,clear_job_status,unregister_job,job_id  # 작업 상태 관리 함수 가져오기

import atexit
import signal
import sys

def scheduled_ticker():
    from crawling.services.daily_stock_prices import update_ticker_data
    print("--scheduled_Automate_Tickers--")
    update_ticker_data()
    print("--scheduled_Automate_Tickers End--")

def scheduled_Article():
    from crawling.services.set_articles import add_new_articles

    if is_job_registered("scheduled_automate"):
            print("Job already registered. scheduled_Article.")
            return
    
    register_job("scheduled_automate")
    print("--scheduled_Article--")
    add_new_articles(isAdmin=False)
    print("--scheduled_Article End--")
    unregister_job("scheduled_automate")

def scheduled_mail():
    from crawling.services.daily_email import daily_email
    print("--scheduled_automate--")
    daily_email()
    
scheduled_task = None
my_schedulers = []
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
        self.start_scheduler()
      

        # 스케줄러 초기화를 별도의 스레드에서 수행
        if settings.DEBUG:
            print("Scheduler ready debug")
            # 스케줄러 초기화를 별도의 스레드에서 수행
            
    

    def start_scheduler(self):
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.executors.pool import ThreadPoolExecutor
        from apscheduler.triggers.interval import IntervalTrigger
        
        from django_apscheduler.jobstores import DjangoJobStore, register_events
        from apscheduler.jobstores.memory import MemoryJobStore
        from apscheduler.triggers.cron import CronTrigger
 

        # 신호 처리기 등록

        if is_job_registered(job_id):
            print("Job already registered. Skipping registration.")
            return
        register_job(job_id)

        print("Registering new job...")

        kst = pytz.timezone('Asia/Seoul')
       
        # (실행할 함수,job id, 타이머, 서버 실행시 즉시 실행 한번 할지 여부 )
        schedulers =[
            (scheduled_ticker,"scheduled_ticker",CronTrigger(hour=23, minute=30, timezone=kst)), #미국장 시작 11:30  pm (한국시간)
            (scheduled_Article,"scheduled_automate",IntervalTrigger(minutes=30)),
            (scheduled_mail,"scheduled_mail_0",CronTrigger(hour=0, minute=0, timezone=kst)),
            (scheduled_mail,"scheduled_mail_1",CronTrigger(hour=12, minute=0, timezone=kst))
        ]

        


        # Scheduler 생성
        for func,now_job_id,trigger in schedulers:
            scheduler = BackgroundScheduler(
                
                jobstores={
                    'default': MemoryJobStore(),
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
            print(f"Scheduler register : {now_job_id}")
            # 1분마다 실행되는 작업 등록
            scheduler.add_job(
                func,
                trigger,
                id=now_job_id,
                replace_existing=True
            )
            my_schedulers.append(scheduler)
            

    def shutdown_scheduler(self, scheduler):
        """스케줄러를 안전하게 종료"""
        clear_job_status()
        print(f"스케줄러 종료 중 (잠시만 기다려주세요)...")
    
        for job in scheduler.get_jobs():
            if scheduler.running:
                scheduler.remove_job(job.id)

        scheduler.shutdown(wait=False)  # 스케줄러 중지
def signal_handler(sig, frame):
    print('Interrupt received, shutting down scheduler...')
    unregister_job("scheduled_automate")
    app_config = TrandlatorConfig('trandlator', sys.modules[__name__])
    for scheduler in my_schedulers:
        if scheduler.running:
            app_config.shutdown_scheduler(scheduler)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)