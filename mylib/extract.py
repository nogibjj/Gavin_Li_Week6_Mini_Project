import os
import requests
# import pandas as pd
import shutil

def extract():
    directory = "extracted"
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)
    url1 = """
    https://raw.githubusercontent.com/nogibjj/Gavin_Li_Week6_Mini_Project/main/resources/state-abbrevs.csv?raw=true
    """
    f1 = "./" + directory + "/state-abbrevs.csv"
    with requests.get(url1) as r:
        with open(f1, "wb") as f:
            f.write(r.content)
    url2 = """
    https://github.com/nogibjj/Gavin_Li_Week6_Mini_Project/blob/main/resources/USCrime.csv?raw=true
    """
    f2 = "./" + directory + "/USCrime.csv"
    with requests.get(url2) as r:
        with open(f2, "wb") as f:
            f.write(r.content)
    return f1, f2

