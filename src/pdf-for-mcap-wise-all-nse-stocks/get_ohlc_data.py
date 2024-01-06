# right now, the lines that are commented out, should be uncommented if you want
# to run this script alone
# one improvement that can be done is: right now i have to define the nse_eq dataframe
# in both of the scripts main.py and get_ohlc_data.py

import pandas as pd
import requests
import time
from datetime import datetime, timedelta
import json
from multiprocessing import Pool
import yfinance as yf

fileUrl ='https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz'
symboldf = pd.read_csv(fileUrl)
symboldf['expiry'] = pd.to_datetime(symboldf['expiry']).apply(lambda x: x.date())
nse_eq = symboldf[(symboldf.last_price.notnull()) & (symboldf.exchange == 'NSE_EQ') & (symboldf.tick_size == 0.05)]
nse_eq.reset_index(drop=True, inplace= True)

# stocks = pd.read_excel('mcap_wise_nse_stocks.xlsx')
# list_trading_symbol = list(stocks['Symbol'])

stock_dict = {}
for i in range(len(nse_eq)):
    stock_dict[nse_eq['tradingsymbol'][i]] = nse_eq['instrument_key'][i]

# list_trading_symbol = list(nse_eq['tradingsymbol'])
# list_instrument_key = list(nse_eq['instrument_key'])
# list_stock_name = list(nse_eq['name'])

# start_index = 0
# end_index = 100

today = datetime.now()
ten_years_ago = today - timedelta(days=365.25 * 10)
five_years_ago = today - timedelta(days=365.25 * 5)
one_year_ago = today - timedelta(days=365)
three_months_ago = today - timedelta(days=45)

today = today.strftime('%Y-%m-%d')
from_date_weekly = five_years_ago.strftime('%Y-%m-%d')
from_date_daily = one_year_ago.strftime('%Y-%m-%d')
from_date_monthly = ten_years_ago.strftime('%Y-%m-%d')
from_date_hourly = three_months_ago.strftime('%Y-%m-%d')
# from_date_weekly = '2018-01-01'
# from_date_monthly = '2014-01-01'
# from_date_daily = ''
# from_date_hourly = ''
base_url = "https://api.upstox.com/v2/"

def getHourlyData(instrument):
    url = f'{base_url}historical-candle/{instrument}/30minute/{today}/{from_date_hourly}' 
    headers = {
        'accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.json()

# data_hourly = yf.download(script, period="3mo", interval="1h")

# def getHourlyData(trading_symbol):


def getDailyData(instrument):
    url = f'{base_url}historical-candle/{instrument}/day/{today}/{from_date_daily}' 
    headers = {
        'accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.json()

def getWeeklyData(instrument):
    url = f'{base_url}historical-candle/{instrument}/week/{today}/{from_date_weekly}' 
    headers = {
        'accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.json()

def getMonthlyData(instrument):
    url = f'{base_url}historical-candle/{instrument}/month/{today}/{from_date_monthly}' 
    headers = {
        'accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_candle_data(trading_symbol):
    try:
        # trading_symbol = list_trading_symbol[i]
        instrument_key = stock_dict[trading_symbol]
        # hourly_data = getHourlyData(instrument_key)
        # hourly_df = pd.DataFrame(hourly_data['data']['candles'])
        # hourly_df.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume', 'NA']
        # hourly_df['Datetime'] = pd.to_datetime(hourly_df['Datetime'])
        # hourly_df.set_index('Datetime', inplace=True)
        # hourly_df = hourly_df.iloc[::-1]
        print(trading_symbol)
        hourly_df = yf.download(trading_symbol+'.NS', period="3mo", interval="1h")
        daily_data = getDailyData(instrument_key)
        daily_df = pd.DataFrame(daily_data['data']['candles'])
        daily_df.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume', 'NA']
        daily_df['Datetime'] = pd.to_datetime(daily_df['Datetime'])
        daily_df.set_index('Datetime', inplace=True)
        daily_df = daily_df.iloc[::-1]
        weekly_data = getWeeklyData(instrument_key)
        weekly_df = pd.DataFrame(weekly_data['data']['candles'])
        weekly_df.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume', 'NA']
        weekly_df['Datetime'] = pd.to_datetime(weekly_df['Datetime'])
        weekly_df.set_index('Datetime', inplace=True)
        weekly_df = weekly_df.iloc[::-1] # reverse the df
        monthly_data = getMonthlyData(instrument_key)
        monthly_df = pd.DataFrame(monthly_data['data']['candles'])
        monthly_df.columns = ['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume', 'NA']
        monthly_df['Datetime'] = pd.to_datetime(monthly_df['Datetime'])
        monthly_df.set_index('Datetime', inplace=True)
        monthly_df = monthly_df.iloc[::-1]
        return trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df)
    except:
        print('Error in ', trading_symbol)
        return None


# if __name__ == "__main__":

#     output = {}

#     start = time.time()

#     l = list(range(len(list_trading_symbol[start_index:end_index])))

#     with Pool(processes=4) as pool:
#         results = pool.map(get_candle_data, l)

#     for result in results:
#         if result is not None:
#             trading_symbol, (weekly_df, monthly_df) = result
#             output[trading_symbol] = [weekly_df, monthly_df]


#     print(f"{time.time() - start} Sec")