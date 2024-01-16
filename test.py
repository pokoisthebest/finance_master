import requests
import pandas as pd
import json
API_KEY = 'bca7fc15d195c77a01ddafa67513ab92'
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
start_date = "2022-01-28"
end_date = "2023-03-17"
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

    return data['symbol']



