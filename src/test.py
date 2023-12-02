import time
import pandas as pd
import yfinance as yf
# from candlestick import download_image
import matplotlib
matplotlib.use('Agg')
import mplfinance as mpf
import gc

start_time = time.time()

dw1 = pd.read_csv('../scripts/dw1.csv')
dw2 = pd.read_csv('../scripts/dw2.csv')
dw3 = pd.read_csv('../scripts/dw3.csv')
dw4 = pd.read_csv('../scripts/dw4.csv')

list_dw1 = list(dw1['CODE'])
list_dw2 = list(dw2['CODE'])
list_dw3 = list(dw3['CODE'])
list_dw4 = list(dw4['CODE'])

import mplfinance as mpf

# GLOBAL VARIABLES

figsize_daily = (9.4,5)
figratio_daily = (1, 0.3)
figscale_daily = 1.0

figsize_hourly = (10,3)
figratio_hourly = (1, 0.2)
figscale_hourly = 0.5

figsize_weekly = (10,3)
figratio_weekly = (1, 0.2)
figscale_weekly = 0.7

figsize_monthly = (10,4)
figratio_monthly = (1, 0.4)
figscale_monthly = 0.7

kwargs1 = dict(type='candle', volume=True, datetime_format='%b-%y', xrotation=0)
kwargs2 = dict(base_mpf_style='yahoo', edgecolor='white', gridcolor='white', 
               facecolor='white', figcolor='white', gridstyle='',gridaxis='vertical')
s = mpf.make_mpf_style(**kwargs2)

def download_image(timeframe, data, script, dw):
    save = dict(fname=f"ohlc-charts/{dw}/{script[:-3]}-{timeframe}.png", dpi=1000, pad_inches=0.25)

    if timeframe == 'daily':
        try:
            mpf.plot(data, title=f"\n{script[:-3]}-{timeframe}", style=s, savefig=save, **kwargs1, 
                 figscale=figscale_daily, figratio=figratio_daily, figsize=figsize_daily)
        except:
            print(f"Error in creating plot for {script} in {timeframe} timeframe!")
    
    if timeframe == 'hourly':
        try:
            mpf.plot(data, title=f"\n{script[:-3]}-{timeframe}", style=s, savefig=save, **kwargs1, 
                 figscale=figscale_hourly, figratio=figratio_hourly, figsize=figsize_hourly)
        except:
            print(f"Error in creating plot for {script} in {timeframe} timeframe!")
        
    if timeframe == 'weekly':
        try:
            mpf.plot(data, title=f"\n{script[:-3]}-{timeframe}", style=s, savefig=save, **kwargs1, 
                 figscale=figscale_weekly, figratio=figratio_weekly, figsize=figsize_weekly)
        except:
            print(f"Error in creating plot for {script} in {timeframe} timeframe!")
        
    if timeframe == 'monthly':
        try:
            mpf.plot(data, title=f"\n{script[:-3]}-{timeframe}", style=s, savefig=save, **kwargs1, 
                 figscale=figscale_monthly, figratio=figratio_monthly, figsize=figsize_monthly)
        except:
            print(f"Error in creating plot for {script} in {timeframe} timeframe!")

# list_dw = list_dw1 + list_dw2 + list_dw3 + list_dw4

for script in list_dw1:
    try:
        data_hourly = yf.download(script, period="3mo", interval="1h")
        print(f"downloading chart for {script} in hourly tf...")
        # download_image('hourly', data_hourly, script, 'dw1')

        save = dict(fname=f"ohlc-charts/dw1/{script[:-3]}-hourly.png", dpi=1000, pad_inches=0.25)
        mpf.plot(data_hourly, title=f"\n{script[:-3]}-hourly", style=s, savefig=save, **kwargs1, 
                 figscale=figscale_hourly, figratio=figratio_hourly, figsize=figsize_hourly)
        # plt.close('all')
        # gc.collect()

        print(f"downloaded chart for {script} in hourly tf!")
    except:
        print("Hourly Error: ", script)
    try:
        data_daily = yf.download(script, period="1y", interval="1d")
        print(f"downloading chart for {script} in daily tf...")
        # download_image('daily', data_daily, script, 'dw1')

        save = dict(fname=f"ohlc-charts/dw1/{script[:-3]}-daily.png", dpi=1000, pad_inches=0.25)
        mpf.plot(data_daily, title=f"\n{script[:-3]}-daily", style=s, savefig=save, **kwargs1, 
                 figscale=figscale_daily, figratio=figratio_daily, figsize=figsize_daily)
        # plt.close('all')
        # gc.collect()

        print(f"downloaded chart for {script} in daily tf!")
    except:
        print("Daily Error: ", script)
    try:
        data_weekly = yf.download(script, period="5y", interval="1wk")
        print(f"downloading chart for {script} in weekly tf...")
        # download_image('weekly', data_weekly, script, 'dw1')

        save = dict(fname=f"ohlc-charts/dw1/{script[:-3]}-weekly.png", dpi=1000, pad_inches=0.25)
        mpf.plot(data_weekly, title=f"\n{script[:-3]}-weekly", style=s, savefig=save, **kwargs1, 
                 figscale=figscale_weekly, figratio=figratio_weekly, figsize=figsize_weekly)
        # plt.close('all')
        # gc.collect()

        print(f"downloaded chart for {script} in weekly tf!")
    except:
        print("Weekly Error: ", script)
    try:
        data_monthly = yf.download(script, period="10y", interval="1mo")
        print(f"downloading chart for {script} in monthly tf...")
        # download_image('monthly', data_monthly, script, 'dw1')

        save = dict(fname=f"ohlc-charts/dw1/{script[:-3]}-monthly.png", dpi=1000, pad_inches=0.25)
        mpf.plot(data_monthly, title=f"\n{script[:-3]}-monthly", style=s, savefig=save, **kwargs1, 
                 figscale=figscale_monthly, figratio=figratio_monthly, figsize=figsize_monthly)
        # plt.close('all')
        # gc.collect()

        print(f"downloaded chart for {script} in monthly tf!")
    except:
        print("Monthly Error: ", script)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")