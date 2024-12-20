import logging
from selenium import webdriver


# 로깅 수준 설정
logging.getLogger('selenium').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)

def get_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument("--disable-notifications")  # 알림 비활성화
    driver = webdriver.Chrome(options=options)
    return driver