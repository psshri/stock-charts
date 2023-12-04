import time
import pandas as pd
import yfinance as yf
from create_candlestick_chart import download_image
from create_pdf import convert_images_to_pdf
from send_pdf import sendit
import asyncio
import nest_asyncio
nest_asyncio.apply()

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

# GET OHLC DATA & CREATE CANDLESTICK CHART

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

# CREATE PDF

print("Creating PDF...")

# Specify the directory containing PNG images
image_directory_dw1 = "ohlc-charts/dw1"
image_directory_dw2 = "ohlc-charts/dw2"
image_directory_dw3 = "ohlc-charts/dw3"
image_directory_dw4 = "ohlc-charts/dw4"
image_directory_myport = "ohlc-charts/myport"

# Specify the output PDF file
output_pdf_dw1 = "ohlc-charts/PDFs/dw1.pdf"
output_pdf_dw2 = "ohlc-charts/PDFs/dw2.pdf"
output_pdf_dw3 = "ohlc-charts/PDFs/dw3.pdf"
output_pdf_dw4 = "ohlc-charts/PDFs/dw4.pdf"
output_pdf_myport = "ohlc-charts/PDFs/myport.pdf"

# Convert images to PDF
convert_images_to_pdf(image_directory_dw1, output_pdf_dw1)
convert_images_to_pdf(image_directory_dw2, output_pdf_dw2)
convert_images_to_pdf(image_directory_dw3, output_pdf_dw3)
convert_images_to_pdf(image_directory_dw4, output_pdf_dw4)
convert_images_to_pdf(image_directory_myport, output_pdf_myport)

print("PDF creation completed!")

# SEND PDF

print("Sending PDFs to Telegram...")

# pdf_file_path_dw1 = 'ohlc-charts/PDFs/dw1.pdf'
# pdf_file_path_dw2 = 'ohlc-charts/PDFs/dw2.pdf'
# pdf_file_path_dw3 = 'ohlc-charts/PDFs/dw3.pdf'
# pdf_file_path_dw4 = 'ohlc-charts/PDFs/dw4.pdf'
# pdf_file_path_myport = 'ohlc-charts/PDFs/myport.pdf'

loop = asyncio.get_event_loop()
loop.run_until_complete(sendit(output_pdf_dw1))
loop.run_until_complete(sendit(output_pdf_dw2))
loop.run_until_complete(sendit(output_pdf_dw3))
loop.run_until_complete(sendit(output_pdf_dw4))
loop.run_until_complete(sendit(output_pdf_myport))

print("PDFs sent to Telegram!")

end_time = time.time()
elapsed_time = end_time - start_time
minutes = round(elapsed_time / 60, 2)
print(f"Time taken: {minutes} minutes")