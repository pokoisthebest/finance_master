import sys
import historical_data as hd
import pandas as pd

def main() -> int:
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
    Assecopol = hd.getData(start_date, end_date, API_KEY, wig20["ASSECOPOL"])
    Assecopol = hd.tabelarizeData(Assecopol)
    print(Assecopol)
    
    return 0





if __name__ == '__main__':
    sys.exit(main())