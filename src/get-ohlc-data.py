import time
import pandas as pd
import yfinance as yf
from candlestick import download_image

start_time = time.time()

dw1    = pd.read_csv('../scripts/dw1.csv')
dw2    = pd.read_csv('../scripts/dw2.csv')
dw3    = pd.read_csv('../scripts/dw3.csv')
dw4    = pd.read_csv('../scripts/dw4.csv')
myport = pd.read_csv('../scripts/myport.csv')

list_dw1    = list(dw1['CODE'])
list_dw2    = list(dw2['CODE'])
list_dw3    = list(dw3['CODE'])
list_dw4    = list(dw4['CODE'])
list_myport = list(myport['CODE'])

# list_dw = list_dw1 + list_dw2 + list_dw3 + list_dw4

for script in list_dw1:
    try:
        data_hourly = yf.download(script, period="3mo", interval="1h")
        print(f"downloading chart for {script} in hourly tf...")
        download_image('4hourly', data_hourly, script, 'dw1')
        print(f"downloaded chart for {script} in hourly tf!")
    except:
        print("Hourly Error: ", script)
    try:
        data_daily = yf.download(script, period="1y", interval="1d")
        print(f"downloading chart for {script} in daily tf...")
        download_image('3daily', data_daily, script, 'dw1')
        print(f"downloaded chart for {script} in daily tf!")
    except:
        print("Daily Error: ", script)
    try:
        data_weekly = yf.download(script, period="5y", interval="1wk")
        print(f"downloading chart for {script} in weekly tf...")
        download_image('2weekly', data_weekly, script, 'dw1')
        print(f"downloaded chart for {script} in weekly tf!")
    except:
        print("Weekly Error: ", script)
    try:
        data_monthly = yf.download(script, period="10y", interval="1mo")
        print(f"downloading chart for {script} in monthly tf...")
        download_image('1monthly', data_monthly, script, 'dw1')
        print(f"downloaded chart for {script} in monthly tf!")
    except:
        print("Monthly Error: ", script)



for script in list_dw2:
    try:
        data_hourly = yf.download(script, period="3mo", interval="1h")
        print(f"downloading chart for {script} in hourly tf...")
        download_image('4hourly', data_hourly, script, 'dw2')
        print(f"downloaded chart for {script} in hourly tf!")
    except:
        print("Hourly Error: ", script)
    try:
        data_daily = yf.download(script, period="1y", interval="1d")
        print(f"downloading chart for {script} in daily tf...")
        download_image('3daily', data_daily, script, 'dw2')
        print(f"downloaded chart for {script} in daily tf!")
    except:
        print("Daily Error: ", script)
    try:
        data_weekly = yf.download(script, period="5y", interval="1wk")
        print(f"downloading chart for {script} in weekly tf...")
        download_image('2weekly', data_weekly, script, 'dw2')
        print(f"downloaded chart for {script} in weekly tf!")
    except:
        print("Weekly Error: ", script)
    try:
        data_monthly = yf.download(script, period="10y", interval="1mo")
        print(f"downloading chart for {script} in monthly tf...")
        download_image('1monthly', data_monthly, script, 'dw2')
        print(f"downloaded chart for {script} in monthly tf!")
    except:
        print("Monthly Error: ", script)



for script in list_dw3:
    try:
        data_hourly = yf.download(script, period="3mo", interval="1h")
        print(f"downloading chart for {script} in hourly tf...")
        download_image('4hourly', data_hourly, script, 'dw3')
        print(f"downloaded chart for {script} in hourly tf!")
    except:
        print("Hourly Error: ", script)
    try:
        data_daily = yf.download(script, period="1y", interval="1d")
        print(f"downloading chart for {script} in daily tf...")
        download_image('3daily', data_daily, script, 'dw3')
        print(f"downloaded chart for {script} in daily tf!")
    except:
        print("Daily Error: ", script)
    try:
        data_weekly = yf.download(script, period="5y", interval="1wk")
        print(f"downloading chart for {script} in weekly tf...")
        download_image('2weekly', data_weekly, script, 'dw3')
        print(f"downloaded chart for {script} in weekly tf!")
    except:
        print("Weekly Error: ", script)
    try:
        data_monthly = yf.download(script, period="10y", interval="1mo")
        print(f"downloading chart for {script} in monthly tf...")
        download_image('1monthly', data_monthly, script, 'dw3')
        print(f"downloaded chart for {script} in monthly tf!")
    except:
        print("Monthly Error: ", script)



for script in list_dw4:
    try:
        data_hourly = yf.download(script, period="3mo", interval="1h")
        print(f"downloading chart for {script} in hourly tf...")
        download_image('4hourly', data_hourly, script, 'dw4')
        print(f"downloaded chart for {script} in hourly tf!")
    except:
        print("Hourly Error: ", script)
    try:
        data_daily = yf.download(script, period="1y", interval="1d")
        print(f"downloading chart for {script} in daily tf...")
        download_image('3daily', data_daily, script, 'dw4')
        print(f"downloaded chart for {script} in daily tf!")
    except:
        print("Daily Error: ", script)
    try:
        data_weekly = yf.download(script, period="5y", interval="1wk")
        print(f"downloading chart for {script} in weekly tf...")
        download_image('2weekly', data_weekly, script, 'dw4')
        print(f"downloaded chart for {script} in weekly tf!")
    except:
        print("Weekly Error: ", script)
    try:
        data_monthly = yf.download(script, period="10y", interval="1mo")
        print(f"downloading chart for {script} in monthly tf...")
        download_image('1monthly', data_monthly, script, 'dw4')
        print(f"downloaded chart for {script} in monthly tf!")
    except:
        print("Monthly Error: ", script)



for script in list_myport:
    try:
        data_hourly = yf.download(script, period="3mo", interval="1h")
        print(f"downloading chart for {script} in hourly tf...")
        download_image('4hourly', data_hourly, script, 'myport')
        print(f"downloaded chart for {script} in hourly tf!")
    except:
        print("Hourly Error: ", script)
    try:
        data_daily = yf.download(script, period="1y", interval="1d")
        print(f"downloading chart for {script} in daily tf...")
        download_image('3daily', data_daily, script, 'myport')
        print(f"downloaded chart for {script} in daily tf!")
    except:
        print("Daily Error: ", script)
    try:
        data_weekly = yf.download(script, period="5y", interval="1wk")
        print(f"downloading chart for {script} in weekly tf...")
        download_image('2weekly', data_weekly, script, 'myport')
        print(f"downloaded chart for {script} in weekly tf!")
    except:
        print("Weekly Error: ", script)
    try:
        data_monthly = yf.download(script, period="10y", interval="1mo")
        print(f"downloading chart for {script} in monthly tf...")
        download_image('1monthly', data_monthly, script, 'myport')
        print(f"downloaded chart for {script} in monthly tf!")
    except:
        print("Monthly Error: ", script)



end_time = time.time()
elapsed_time = end_time - start_time
minutes = round(elapsed_time / 60, 2)
print(f"Time taken: {minutes} minutes")