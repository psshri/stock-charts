# import time
import pandas as pd
import yfinance as yf
# from create_candlestick_chart import download_image
# from create_pdf import convert_images_to_pdf
# from send_pdf import sendit
# import asyncio
# import nest_asyncio
# import multiprocessing
# nest_asyncio.apply()

# dw1    = pd.read_csv('../scripts/dw1.csv')
# dw2    = pd.read_csv('../scripts/dw2.csv')
# dw3    = pd.read_csv('../scripts/dw3.csv')
# dw4    = pd.read_csv('../scripts/dw4.csv')
# myport = pd.read_csv('../scripts/myport.csv')

# list_dw1    = list(dw1['CODE'])
# list_dw2    = list(dw2['CODE'])
# list_dw3    = list(dw3['CODE'])
# list_dw4    = list(dw4['CODE'])
# list_myport = list(myport['CODE'])

# list_all = list_dw1 + list_dw2 + list_dw3 + list_dw4

def get_ohlc_data(script):
    data_hourly = None
    data_daily = None
    data_weekly = None
    data_monthly = None
    try:
        data_hourly = yf.download(script, period="3mo", interval="1h")
    except:
        print("Hourly Error: ", script)
    try:
        data_daily = yf.download(script, period="1y", interval="1d")
    except:
        print("Daily Error: ", script)
    try:
        data_weekly = yf.download(script, period="5y", interval="1wk")
    except:
        print("Weekly Error: ", script)
    try:
        data_monthly = yf.download(script, period="10y", interval="1mo")
    except:
        print("Monthly Error: ", script)
    return data_hourly, data_daily, data_weekly, data_monthly

def process_script(script):
    try:
        result = get_ohlc_data(script)
        return script, result
    except Exception as e:
        return script, f"Error: {str(e)}"
    
# if __name__ == "__main__":
#     num_processes = 4

#     with multiprocessing.Pool(num_processes) as pool:
#         results = pool.map(process_script, list_all)

#     for script, result in results:
#         if isinstance(result, str) and "Error" in result:
#             print(f"Error processing {script}: {result}")
#         else:
#             data_hourly, data_daily, data_weekly, data_monthly = result