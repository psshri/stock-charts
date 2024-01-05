from get_ohlc_data import get_candle_data
from create_candlestick_chart import download_image
import pandas as pd
import requests
import time
from datetime import datetime
import json
from multiprocessing import Pool
import os
from create_pdf import convert_images_to_pdf
# import asyncio
# import nest_asyncio
# nest_asyncio.apply()
# from send_pdf import sendit

start_index = 2100
end_index = 2138

# start_index = 0
# end_index = 100
folder_name = f"{start_index+1}-{end_index}"
os.makedirs(f"ohlc-charts/{folder_name}", exist_ok=True)

fileUrl ='https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz'
symboldf = pd.read_csv(fileUrl)
symboldf['expiry'] = pd.to_datetime(symboldf['expiry']).apply(lambda x: x.date())
nse_eq = symboldf[(symboldf.last_price.notnull()) & (symboldf.exchange == 'NSE_EQ') & (symboldf.tick_size == 0.05)]
nse_eq.reset_index(drop=True, inplace= True)

list_trading_symbol = list(nse_eq['tradingsymbol'])
list_instrument_key = list(nse_eq['instrument_key'])
list_stock_name = list(nse_eq['name'])

if __name__ == "__main__":

    # output = {}

    start = time.time()

    # l = list(range(len(list_trading_symbol[start_index:end_index])))
    l = list(range(start_index, end_index))

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, l)

    for result in results:
        if result is not None:
            trading_symbol, (weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('2weekly', weekly_df, trading_symbol, folder_name)
            download_image('1monthly', monthly_df, trading_symbol, folder_name)


            
    # Specify the directory containing PNG images
    image_directory = f"ohlc-charts/{folder_name}"

    # Specify the output PDF file
    output_pdf = f"ohlc-charts/PDFs/{folder_name}.pdf"

    # CREATE PDF
    print("Creating PDF...")

    # Convert images to PDF
    convert_images_to_pdf(image_directory, output_pdf)

    print("PDF creation completed!")

    # # SEND PDF
    # print("Sending PDFs to Telegram...")

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(sendit(output_pdf))

    # print("PDFs sent to Telegram!")



    print(f"{time.time() - start} Sec")