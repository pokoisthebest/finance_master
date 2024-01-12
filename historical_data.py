import requests
import pandas as pd
import json

API_KEY = 'FEYSO37WOLRNL4UZ'
wig20 = {
    "ASSECOPOL" : "ACP",
    "ALLEGRO" : "ALE",
    "ALIOR" : "ALR",
    "CDPROJEKT" : "CDR",
    "CYFRPLSAT" : "CPS",
    "DINOPL" : "DNP",
    "JSW" : "JSW",
    "KGHM" : "KGH",
    "KRUK" : "KRU",
    "KETY" : "KTY",
    "LPP" : "LPP",
    "MBANK" : "MBK",
    "ORANGEPL" : "OPL",
    "PEPCO" : "PCO",
    "PEKAO" : "PEO",
    "PGE" : "PGE",
    "PKNORLEN" : "PKN",
    "PKOBP" : "PKO",
    "PZU" : "PZU",
    "SANPL" : "SPL"
}
def getData(company: str):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={company}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()
    # data = pd.json_normalize(data['Monthly Time Series'])
    # return type(data)
    new_dict = {}
    for key in data['Monthly Time Series']:
        print(key,':' ,data['Monthly Time Series'][key]['4. close'])

    # return data["Monthly Time Series"]["2017-10-19"]
    # return new_dict

print(getData(wig20["ALIOR"]))