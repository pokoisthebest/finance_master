from os import listdir
from os.path import isfile, join
import pandas as pd
# from IPython import display
mypath = "data/"
# Returns dictionary of dataframes 
def load():
    # Load historical data, convert it to df and add to Companies dictionary 
    Companies = {}
    files = get_file_list()
    for file in files:
        df = pd.read_csv(mypath + file)
        df['Date'] = pd.to_datetime(df["Date"])
        # print(df)
        Companies.update({file: df})
    return Companies

def get_file_list():
    file_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return file_list
# Companies = load()
# print(Companies["ALLEGRO.csv"])
# print(Companies["PEO Historical Data.csv"][Companies["PEO Historical Data.csv"]["Date"].dt.year == 2020])
