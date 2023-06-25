#### Etherscan API tracker ####
# python version = 3.11.2

import requests
import json
import time
from datetime import datetime
import pytz
import pandas as pd


# gas tracker
def gas_tracker(p:int):
    SL_tz = pytz.timezone('Asia/Colombo')
    df = pd.DataFrame(columns=['time','low','mid','high'])

    i = 1
    while i < p+1:
        response = requests.get('https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=AER6M2C3436231IGT7SV7JZ2URFYFX7MZ1').text
        response_info = json.loads(response)
        low = response_info['result']['SafeGasPrice']
        low = int(low)
        mid = response_info['result']['ProposeGasPrice']
        mid = int(mid)
        high = response_info['result']['FastGasPrice']
        high = int(high)
        t = datetime.now(SL_tz).strftime('%Y-%m-%d %H-%M-%S')

        dr = pd.DataFrame({'time':t, 'low':low, 'mid':mid, 'high':high}, index=[0])
        df = pd.concat([df, dr], ignore_index=True)

        print(str(i) + ' Record saved.')
        i += 1
        time.sleep(58)

    #saving collected data    
    df.to_csv('gpfile.csv')
    return df

def clean_data(data):
    if data is None:
        data = pd.read_csv('gpfile.csv')

    data['low'] = data['low'].astype('int')
    data['mid'] = data['mid'].astype('int')
    data['high'] = data['high'].astype('int')
    data['time'] = pd.to_datetime(data['time'], format = '%Y-%m-%d %H-%M-%S')
    try:
        data = data.drop(['Unnamed: 0'], axis=1)
    except:
        data

    return data