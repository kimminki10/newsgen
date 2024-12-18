from celery import shared_task

@shared_task
def my_periodic_task():
    print("1분마다 실행되는 함수입니다!")
    # 여기에 원하는 로직을 작성합니다
    return "작업 완료"
