from crawling.db_service_folder import db_services as ds
import yfinance as yf
import pandas as pd

def add_new_tickers():
    print("티커 이름들 가져오기기")
    ticker_names = get_ticker_names()
    print("티커 값들 가져오기기")
    result, valid_tickers, invalid_tickers = validate_tickers(ticker_names)
    print("디비에 저장하기기")
    print(ds.add_tickers_to_db(result))

def validate_tickers(ticker_list, period="5d"):
    # Fetch minimal data for the ticker list
    data = yf.download(ticker_list, period=period, group_by="ticker", progress=False, actions=False)
    print(data)
    # Initialize lists for valid and invalid tickers
    valid_tickers = []
    invalid_tickers = []
    result = {}
    # Iterate through the tickers and validate in a single loop
    for ticker in data.columns.levels[0]:
        if not data[ticker]['Open'].isna().all():  # Check if the 'Open' column is not all NaN
            valid_tickers.append(ticker)
            ################################################
            # Extract 'Close' prices for the ticker and drop NaN values
            close_prices = data[ticker]['Close'].dropna()
            
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
            ################################################
        else:
            invalid_tickers.append(ticker)

    return result, valid_tickers, invalid_tickers

def get_ticker_names(csv='combined_tickers_large.csv'):
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
    # Flatten the dictionary into a single list of tickers
    all_tickers_list = [ticker for category in all_tickers.values() for ticker in category]

    # Print the resulting list
    combined_df = pd.read_csv(f"crawling/services/ticker_csv/{csv}")
    symbols = list(combined_df['Symbol'])
    all_tickers_list.extend(symbols)
    return all_tickers_list

add_new_tickers()