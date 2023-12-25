import pandas as pd
import requests
import time
from datetime import datetime

fileUrl ='https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz'
symboldf = pd.read_csv(fileUrl)
symboldf['expiry'] = pd.to_datetime(symboldf['expiry']).apply(lambda x: x.date())
nse_eq = symboldf[(symboldf.last_price.notnull()) & (symboldf.exchange == 'NSE_EQ') & (symboldf.tick_size == 0.05)]
nse_eq.reset_index(drop=True, inplace= True)

list_trading_symbol = list(nse_eq['tradingsymbol'])
list_instrument_key = list(nse_eq['instrument_key'])
list_stock_name = list(nse_eq['name'])

today = datetime.now()
today = today.strftime('%Y-%m-%d')
from_date = '2014-01-01'
base_url = "https://api.upstox.com/v2/"

def getWeeklyData(instrument):
    url = f'{base_url}historical-candle/{instrument}/week/{today}/{from_date}' 
    headers = {
        'accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.json()

def getMonthlyData(instrument):
    url = f'{base_url}historical-candle/{instrument}/month/{today}/{from_date}' 
    headers = {
        'accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    return response.json()


output = {}

start = time.time()

for i in range(len(list_trading_symbol)):
    trading_symbol = list_trading_symbol[i]
    instrument_key = list_instrument_key[i]
    try:
        weekly_data = getWeeklyData(instrument_key)
        weekly_df = pd.DataFrame(weekly_data['data']['candles'])
        monthly_data = getMonthlyData(instrument_key)
        monthly_df = pd.DataFrame(monthly_data['data']['candles'])
        # print(i, trading_symbol, len(weekly_data['data']['candles']))
        print(f"{i}-{trading_symbol}-weekly-{len(weekly_df)}")
        print(f"{i}-{trading_symbol}-monthly-{len(monthly_df)}")
        # print(i, trading_symbol, len(monthly_data['data']['candles']))
        output[trading_symbol] = (weekly_df, monthly_df)
    except:
        print('Error in ', trading_symbol)

print(f"{time.time() - start} Sec")