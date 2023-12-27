# right now, the lines that are commented out, should be uncommented if you want
# to run this script alone
# one improvement that can be done is: right now i have to define the nse_eq dataframe
# in both of the scripts main.py and get_ohlc_data.py

import pandas as pd
import requests
import time
from datetime import datetime
import json
from multiprocessing import Pool

fileUrl ='https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz'
symboldf = pd.read_csv(fileUrl)
symboldf['expiry'] = pd.to_datetime(symboldf['expiry']).apply(lambda x: x.date())
nse_eq = symboldf[(symboldf.last_price.notnull()) & (symboldf.exchange == 'NSE_EQ') & (symboldf.tick_size == 0.05)]
nse_eq.reset_index(drop=True, inplace= True)

list_trading_symbol = list(nse_eq['tradingsymbol'])
list_instrument_key = list(nse_eq['instrument_key'])
list_stock_name = list(nse_eq['name'])

# start_index = 0
# end_index = 100

today = datetime.now()
today = today.strftime('%Y-%m-%d')
from_date_weekly = '2018-01-01'
from_date_monthly = '2014-01-01'
base_url = "https://api.upstox.com/v2/"

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

def get_candle_data(i):
    try:
        trading_symbol = list_trading_symbol[i]
        instrument_key = list_instrument_key[i]
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
        return trading_symbol, (weekly_df, monthly_df)
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