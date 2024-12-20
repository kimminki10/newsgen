from crawling.services import ticker_service as ts
from crawling.db_service_folder import db_services as ds

def update_ticker_data():
    #속도가 많이 느리긴 한데 그래도 자주 실행하는 함수는 아니다.
    #get all ticker names
    ticker_names = ds.get_all_ticker_names()
    #get all ticker's new data based on ticker names
    tickers_data = ts.tickers_price_diff(ticker_names)

    #apply changes to db
    ds.update_ticker_prices(tickers_data)
    print("done")
    
#if __name__ == "__main__":
    #update_ticker_data()