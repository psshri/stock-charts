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
import asyncio
import nest_asyncio
nest_asyncio.apply()
from send_pdf import sendit

# start_index = 2100
# end_index = 2138

# start_index = 0
# end_index = 100
# folder_name = f"{start_index+1}-{end_index}"
folder_name1 = "risen_strong"
folder_name2 = "veryGoodSetupAll"
folder_name3 = "potentialInComingDays"
folder_name4 = "potentialInComingWeeks"
folder_name5 = "inConsolidationRN"
folder_name6 = "downTrendButGoodCP"
folder_name7 = "myPort"
folder_name8 = "placeGTT"
os.makedirs(f"ohlc-charts/{folder_name1}", exist_ok=True)
os.makedirs(f"ohlc-charts/{folder_name2}", exist_ok=True)
os.makedirs(f"ohlc-charts/{folder_name3}", exist_ok=True)
os.makedirs(f"ohlc-charts/{folder_name4}", exist_ok=True)
os.makedirs(f"ohlc-charts/{folder_name5}", exist_ok=True)
os.makedirs(f"ohlc-charts/{folder_name6}", exist_ok=True)
os.makedirs(f"ohlc-charts/{folder_name7}", exist_ok=True)
os.makedirs(f"ohlc-charts/{folder_name8}", exist_ok=True)

watchlist = pd.read_csv('../mcap-wise-all-nse-stocks/ohlc-charts/PDFs/watchlist.csv')

risen_strong           = list(watchlist[watchlist['risen&strong'].notna()]['risen&strong'])
veryGoodSetupAll       = list(watchlist[watchlist['veryGoodSetupAll'].notna()]['veryGoodSetupAll'])
potentialInComingDays  = list(watchlist[watchlist['potentialInComingDays'].notna()]['potentialInComingDays'])
potentialInComingWeeks = list(watchlist[watchlist['potentialInComingWeeks'].notna()]['potentialInComingWeeks'])
inConsolidationRN      = list(watchlist[watchlist['inConsolidationRN'].notna()]['inConsolidationRN'])
downTrendButGoodCP     = list(watchlist[watchlist['downTrendButGoodCP'].notna()]['downTrendButGoodCP'])
myPort                 = list(watchlist[watchlist['myPort'].notna()]['myPort'])
placeGTT               = list(watchlist[watchlist['placeGTT'].notna()]['placeGTT'])

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

    # l1 = list(range(len(risen_strong)))
    # l = list(range(start_index, end_index))

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, risen_strong)

    for result in results:
        if result is not None:
            trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('4hourly', hourly_df, trading_symbol, folder_name1)
            download_image('3daily', daily_df, trading_symbol, folder_name1)
            download_image('2weekly', weekly_df, trading_symbol, folder_name1)
            download_image('1monthly', monthly_df, trading_symbol, folder_name1)

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, veryGoodSetupAll)

    for result in results:
        if result is not None:
            trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('4hourly', hourly_df, trading_symbol, folder_name2)
            download_image('3daily', daily_df, trading_symbol, folder_name2)
            download_image('2weekly', weekly_df, trading_symbol, folder_name2)
            download_image('1monthly', monthly_df, trading_symbol, folder_name2)

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, potentialInComingDays)

    for result in results:
        if result is not None:
            trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('4hourly', hourly_df, trading_symbol, folder_name3)
            download_image('3daily', daily_df, trading_symbol, folder_name3)
            download_image('2weekly', weekly_df, trading_symbol, folder_name3)
            download_image('1monthly', monthly_df, trading_symbol, folder_name3)

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, potentialInComingWeeks)

    for result in results:
        if result is not None:
            trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('4hourly', hourly_df, trading_symbol, folder_name4)
            download_image('3daily', daily_df, trading_symbol, folder_name4)
            download_image('2weekly', weekly_df, trading_symbol, folder_name4)
            download_image('1monthly', monthly_df, trading_symbol, folder_name4)

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, inConsolidationRN)

    for result in results:
        if result is not None:
            trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('4hourly', hourly_df, trading_symbol, folder_name5)
            download_image('3daily', daily_df, trading_symbol, folder_name5)
            download_image('2weekly', weekly_df, trading_symbol, folder_name5)
            download_image('1monthly', monthly_df, trading_symbol, folder_name5)

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, downTrendButGoodCP)

    for result in results:
        if result is not None:
            trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('4hourly', hourly_df, trading_symbol, folder_name6)
            download_image('3daily', daily_df, trading_symbol, folder_name6)
            download_image('2weekly', weekly_df, trading_symbol, folder_name6)
            download_image('1monthly', monthly_df, trading_symbol, folder_name6)

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, myPort)

    for result in results:
        if result is not None:
            trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('4hourly', hourly_df, trading_symbol, folder_name7)
            download_image('3daily', daily_df, trading_symbol, folder_name7)
            download_image('2weekly', weekly_df, trading_symbol, folder_name7)
            download_image('1monthly', monthly_df, trading_symbol, folder_name7)

    with Pool(processes=4) as pool:
        results = pool.map(get_candle_data, placeGTT)

    for result in results:
        if result is not None:
            trading_symbol, (hourly_df, daily_df, weekly_df, monthly_df) = result
            # output[trading_symbol] = [weekly_df, monthly_df]
            download_image('4hourly', hourly_df, trading_symbol, folder_name8)
            download_image('3daily', daily_df, trading_symbol, folder_name8)
            download_image('2weekly', weekly_df, trading_symbol, folder_name8)
            download_image('1monthly', monthly_df, trading_symbol, folder_name8)


            
    # Specify the directory containing PNG images
    image_directory1 = f"ohlc-charts/{folder_name1}"
    image_directory2 = f"ohlc-charts/{folder_name2}"
    image_directory3 = f"ohlc-charts/{folder_name3}"
    image_directory4 = f"ohlc-charts/{folder_name4}"
    image_directory5 = f"ohlc-charts/{folder_name5}"
    image_directory6 = f"ohlc-charts/{folder_name6}"
    image_directory7 = f"ohlc-charts/{folder_name7}"
    image_directory8 = f"ohlc-charts/{folder_name8}"


    # Specify the output PDF file
    output_pdf1 = f"ohlc-charts/PDFs/{folder_name1}.pdf"
    output_pdf2 = f"ohlc-charts/PDFs/{folder_name2}.pdf"
    output_pdf3 = f"ohlc-charts/PDFs/{folder_name3}.pdf"
    output_pdf4 = f"ohlc-charts/PDFs/{folder_name4}.pdf"
    output_pdf5 = f"ohlc-charts/PDFs/{folder_name5}.pdf"
    output_pdf6 = f"ohlc-charts/PDFs/{folder_name6}.pdf"
    output_pdf7 = f"ohlc-charts/PDFs/{folder_name7}.pdf"
    output_pdf8 = f"ohlc-charts/PDFs/{folder_name8}.pdf"


    # CREATE PDF
    print("Creating PDF...")

    # Convert images to PDF
    convert_images_to_pdf(image_directory1, output_pdf1)
    convert_images_to_pdf(image_directory2, output_pdf2)
    convert_images_to_pdf(image_directory3, output_pdf3)
    convert_images_to_pdf(image_directory4, output_pdf4)
    convert_images_to_pdf(image_directory5, output_pdf5)
    convert_images_to_pdf(image_directory6, output_pdf6)
    convert_images_to_pdf(image_directory7, output_pdf7)
    convert_images_to_pdf(image_directory8, output_pdf8)


    print("PDF creation completed!")

    # SEND PDF
    print("Sending PDFs to Telegram...")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(sendit(output_pdf1))
    loop.run_until_complete(sendit(output_pdf2))
    loop.run_until_complete(sendit(output_pdf3))
    loop.run_until_complete(sendit(output_pdf4))
    loop.run_until_complete(sendit(output_pdf5))
    loop.run_until_complete(sendit(output_pdf6))
    loop.run_until_complete(sendit(output_pdf7))
    loop.run_until_complete(sendit(output_pdf8))

    print("PDFs sent to Telegram!")



    print(f"{round((time.time() - start)/60, 2)} Mins")