import requests
import pandas as pd
import json


def getData(start_date: str, end_date: str, API_KEY, company: str):
    """
    Retrieves historical price data for a given company within a specified date range.

    Parameters:
    - start_date (str): The start date of the data range in the format 'YYYY-MM-DD'.
    - end_date (str): The end date of the data range in the format 'YYYY-MM-DD'.
    - API_KEY: The API key for accessing the financial data.
    - company (str): The symbol or ticker of the company.

    Returns:
    - data (dict): A dictionary containing the historical price data for the company.
    """
    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{company}?from={start_date}&to={end_date}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()
    return data

def tabelarizeData(data):
    """
    Converts historical data into a pandas DataFrame.

    Args:
        data (dict): A dictionary containing historical data.

    Returns:
        pandas.DataFrame: A DataFrame with columns 'Date' and 'Value', representing the date and closing value respectively.
        None: If an exception occurs during the conversion process.
    """
    data['symbol'] = {}
    try:
        for day in data["historical"]:
            data['symbol'].update({day['date'] : day['close']})
        df = pd.DataFrame(columns=['Date', 'Value'])
        df['Date'] =  data['symbol'].keys()
        df['Value'] =  data['symbol'].values()
    except:
        return None
    return df



