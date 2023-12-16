from get_ohlc_data import process_script
import multiprocessing
import pandas as pd
import time

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

list_all = list_dw1 + list_dw2 + list_dw3 + list_dw4

if __name__ == "__main__":
    start_time = time.time()
    num_processes = 4

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(process_script, list_all)

    for script, result in results:
        if isinstance(result, str) and "Error" in result:
            print(f"Error processing {script}: {result}")
        else:
            data_hourly, data_daily, data_weekly, data_monthly = result

    end_time = time.time()
    elapsed_time = end_time - start_time
    seconds = round(elapsed_time, 2)
    print(f"Time taken: {seconds} seconds")