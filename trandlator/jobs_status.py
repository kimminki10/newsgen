import threading
# 전역 변수로 작업 상태 저장
registered_jobs = {}

job_id = "automate_job"  # 작업의 고유 ID

def is_job_registered(job_id):
    global registered_jobs
    """작업이 등록되었는지 확인"""
    return registered_jobs.get(job_id, False)

def register_job(job_id):
    global registered_jobs
    """작업을 등록"""
    registered_jobs[job_id] = True

def unregister_job(job_id):
    global registered_jobs
    """작업을 해제"""
    if job_id in registered_jobs:
        del registered_jobs[job_id]

def clear_job_status():
    global registered_jobs
    """모든 작업 상태 초기화 (테스트용 또는 서버 재시작 시)"""
    registered_jobs.clear()
