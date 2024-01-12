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

# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={wig20["ALIOR"]}&apikey={API_KEY}'
# r = requests.get(url)
# f = open('alr.json')
with open('alr.json') as f:
    data = json.load(f)
# print(data['Monthly Time Series'])
for key in data['Monthly Time Series']:
    print(key,':' ,data['Monthly Time Series'][key]['4. close'])
# f.close()