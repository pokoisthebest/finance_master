import sys
import historical_data as hd
import pandas as pd
import gui

def main() -> int:
    """
    Main function that retrieves financial data for companies in the WIG20 index.

    Returns:
        int: The exit code of the function.
    """
    API_KEY = 'bca7fc15d195c77a01ddafa67513ab92'
    wig20 = {
        "ASSECOPOL" : "ACP",
        "ALLEGRO" : "ALE",
        "ALIOR" : "ALR",
        "CDPROJEKT" : "CDR",
        "CYFRPLSAT" : "CPS",
        "DINOPL" : "DNP",
        "JSW" : "JSW.WA",
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
    wig20_tables = [key for key in wig20]
    wig20_tables = [hd.tabelarizeData(hd.getData(start_date, end_date, API_KEY, wig20[company])) for company in wig20_tables]
    [print(company) for company in wig20_tables]
    gui.make_gui()
    return 0





if __name__ == '__main__':
    sys.exit(main())