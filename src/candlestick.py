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

# save_dw1 = dict(fname="ohlc-charts/dw1/test1.png", dpi=1000, pad_inches=0.25)

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