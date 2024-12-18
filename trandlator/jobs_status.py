# trandlator/job_status.py

# 전역 변수로 작업 상태 저장
registered_jobs = {}

def is_job_registered(job_id):
    """작업이 등록되었는지 확인"""
    return registered_jobs.get(job_id, False)

def register_job(job_id):
    """작업을 등록"""
    registered_jobs[job_id] = True

def clear_job_status():
    """모든 작업 상태 초기화 (테스트용 또는 서버 재시작 시)"""
    registered_jobs.clear()
