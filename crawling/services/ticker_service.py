
import yfinance as yf
import pandas as pd



def ticker_price_diff(ticker: str):
    """
    RETURNS 
        last_price: 마지막 가격
        before_last_price: 마지막 전의 가격
        price diffence in USD: 전날과 전전날의 차이
        price difference in percentage: 퍼센티지 기준의 차이
        last_price_date: 전날의 정확한 날짜 (한국시간)
        before_last_date: 전전날의 정확한 날짜 (한국시간)
    """
    ticker_data = yf.Ticker(ticker).history(period="5d").dropna(subset=["Close"])
    if not ticker_data.empty and len(ticker_data) >= 2:
        #prices
        last_price = ticker_data.Close.iloc[-1] #getting the last closed price
        before_last_price = ticker_data.Close.iloc[-2] # getting the before last closed price
        #두자리수를 원할지
        last_price = round(last_price, 2)
        before_last_price = round(before_last_price, 2)
        
        # dates
        #TODO: decide if EST date or Korean Date will be used
        original_dates = pd.to_datetime(ticker_data.index)
        korean_dates = original_dates.tz_convert('Asia/Seoul')
        last_price_date = korean_dates[-1] #getting the last closed price Date
        before_last_date = korean_dates[-2] #getting the before last closed Date
        #calculations
        difference = last_price - before_last_price
        percentage = difference / before_last_price * 100
        #두자리수를 원할지
        difference = round(difference, 2)
        percentage = round(percentage, 2)
        return last_price, before_last_price, difference, percentage, last_price_date, before_last_date
    return None

def tickers_price_diff(tickers: list[str]):
    """
    RETURNS 
        last_price: 마지막 가격
        before_last_price: 마지막 전의 가격
        price diffence in USD: 전날과 전전날의 차이
        price difference in percentage: 퍼센티지 기준의 차이
        last_price_date: 전날의 정확한 날짜 (한국시간)
        before_last_date: 전전날의 정확한 날짜 (한국시간)
    """
    # Fetch historical data using yfinance
    data = yf.Tickers(tickers).history(period="5d")

    # Initialize result dictionary
    result = {}

    for ticker in tickers:
        try:
            # Extract 'Close' prices for the ticker and drop NaN values
            close_prices = data['Close'][ticker].dropna()
            
            # Ensure we have at least two valid prices
            if len(close_prices) >= 2:
                # Extract last price and before last price
                last_price = close_prices.iloc[-1]
                before_last_price = close_prices.iloc[-2]
                # Calculate price difference
                price_difference = last_price - before_last_price
                percentage_difference = (price_difference / before_last_price) * 100
                
                #두자릿수로 계산
                last_price = round(last_price, 2)
                before_last_price = round(before_last_price, 2)
                price_difference = round(price_difference, 2)
                percentage_difference = round(percentage_difference, 2)
                
                # Store results
                result[ticker] = {
                    "last_price": last_price,
                    "before_last_price": before_last_price,
                    "price_difference": price_difference,
                    "percentage_difference": percentage_difference,
                    "last_price_date": close_prices.index[-1],
                    "before_last_price_date": close_prices.index[-2]
                }
            else:
                # result[ticker] = "Not enough data"
                print(f"{ticker} does not have Enough price_data")

        except KeyError:
            result[ticker] = "Ticker not found"
    
    return result

    
"""
if __name__ == "__main__":
    # Major U.S. Indices
    sp500_ticker = "^GSPC"    # S&P 500: Tracks the top 500 large-cap U.S. companies
    dji_ticker = "^DJI"       # Dow Jones Industrial Average: 30 blue-chip U.S. companies
    rus_2000_ticker = "^RUT"  # Russell 2000: Tracks small-cap U.S. companies
    nas_100_ticker = "^NDX"   # Nasdaq 100: Top 100 non-financial companies on Nasdaq
    nas_composite_ticker = "^IXIC"  # Nasdaq Composite: All Nasdaq-listed stocks
    vix_ticker = "^VIX"       # S&P 500 Volatility Index: Measures market volatility
    wilshire_5000_ticker = "^W5000"  # Wilshire 5000: Broadest measure of U.S. stock market

    # Sector-Specific ETFs (Tracks U.S. stock market sectors)
    tech_ticker = "XLK"           # Technology Sector
    financials_ticker = "XLF"     # Financials Sector
    healthcare_ticker = "XLV"     # Healthcare Sector
    energy_ticker = "XLE"         # Energy Sector
    industrials_ticker = "XLI"    # Industrials Sector
    utilities_ticker = "XLU"      # Utilities Sector
    consumer_disc_ticker = "XLY"  # Consumer Discretionary Sector
    consumer_staples_ticker = "XLP"  # Consumer Staples Sector
    real_estate_ticker = "XLRE"   # Real Estate Sector
    materials_ticker = "XLB"      # Materials Sector

    # Bond and Treasury Market
    ten_year_treasury_ticker = "^TNX"  # 10-Year U.S. Treasury Yield
    thirty_year_treasury_ticker = "^TYX"  # 30-Year U.S. Treasury Yield
    agg_bond_index_ticker = "AGG"  # U.S. Aggregate Bond Index
    corporate_bonds_ticker = "LQD"  # U.S. Investment-Grade Corporate Bonds

    # Commodity and Inflation-Related
    gold_ticker = "GC=F"          # Gold Futures
    crude_oil_ticker = "CL=F"     # Crude Oil Futures (WTI)
    usd_index_ticker = "DX-Y.NYB" # U.S. Dollar Index
    inflation_protected_ticker = "TIP"  # U.S. Treasury Inflation-Protected Securities

    # Other U.S. Market Indices
    dow_transport_ticker = "^DJT"  # Dow Jones Transportation Average
    dow_utilities_ticker = "^DJU"  # Dow Jones Utilities Average
    sp_midcap_ticker = "^MID"      # S&P MidCap 400
    sp_smallcap_ticker = "^SML"    # S&P SmallCap 600

    # Print all tickers for confirmation
    all_tickers = {
        "Major Indices": [sp500_ticker, dji_ticker, rus_2000_ticker, nas_100_ticker, nas_composite_ticker, vix_ticker, wilshire_5000_ticker],
        "Sector ETFs": [tech_ticker, financials_ticker, healthcare_ticker, energy_ticker, 
                        industrials_ticker, utilities_ticker, consumer_disc_ticker, 
                        consumer_staples_ticker, real_estate_ticker, materials_ticker],
        "Bonds and Treasury": [ten_year_treasury_ticker, thirty_year_treasury_ticker, agg_bond_index_ticker, corporate_bonds_ticker],
        "Commodities and Inflation": [gold_ticker, crude_oil_ticker, usd_index_ticker, inflation_protected_ticker],
        "Other Indices": [dow_transport_ticker, dow_utilities_ticker, sp_midcap_ticker, sp_smallcap_ticker]
    }
    #s&p500
    sp500_ticker = "^GSPC"
    print(ticker_price_diff(sp500_ticker))
    #print(tickers_price_diff(all_tickers['Major Indices']))
"""