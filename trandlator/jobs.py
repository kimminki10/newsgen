import logging
from crawling.automate_crawling import automate_crawler
from crawling.services.ticker_service import tickers_price_diff
from crawling.db_service_folder import db_services as ds
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
    print("Tickers Schedule Start!")
    all_ticker_names = ds.get_all_ticker_names()
    print(f"Ticker Names : {all_ticker_names}")
    if(len(all_ticker_names) > 0):
        all_tickers_price_diff = tickers_price_diff(all_ticker_names)
        print(f"Ticker All : {all_tickers_price_diff}")
   
    print("Tickers Schedule End!")

