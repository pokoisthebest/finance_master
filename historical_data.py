import requests
import pandas as pd
import json

#TODO check how to declare default values to functions
def getData(start_date: str, end_date: str, API_KEY, company: str):
    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{company}?from={start_date}&to={end_date}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()
    return data

def tabelarizeData(data):
    data['symbol'] = {}
    for day in data['historical']:
        # print(f"{day['date']} : {day['close']} \n")
        data['symbol'].update({day['date'] : day['close']})
    df = pd.DataFrame(columns=['Date', 'Value'])
    df['Date'] =  data['symbol'].keys()
    df['Value'] =  data['symbol'].values()

    return df



