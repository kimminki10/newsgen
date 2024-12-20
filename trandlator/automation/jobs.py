import logging
from crawling.automate_crawling import automate_crawler
from crawling.services.ticker_service import tickers_price_diff
from crawling.db_service_folder import db_services as ds
from crawling.services.daily_email import daily_email
from crawling.services.daily_stock_prices import update_ticker_data
logger = logging.getLogger(__name__)

# 로그 레벨을 WARNING으로 설정하여 디버그 로그 비활성화
logging.getLogger("yfinance").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy").setLevel(logging.WARNING)  # SQLAlchemy 사용 시

# Crawling and openai automate
def Automate():
    print("Article Schedule Start!")
    automate_crawler()
    print("Article Schedule End!")

# Tickers automate
def Automate_Tickers():
    #장시간 끝날때 한번만 실행 -> 여유시간 30분 두고 실행 
    print("Tickers Schedule Start!")
    update_ticker_data()
    print("Tickers Schedule End!")

def Automate_Mail():
    print("Mail Schedule Start!")
    print("Mail Schedule End!")