import logging
from crawling.automate_crawling import automate_crawler
logger = logging.getLogger(__name__)

def Automate():
    print("스케줄러 Start!")
    automate_crawler()
    print("스케줄러 End!")
