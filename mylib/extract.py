import os
import requests
import pandas as pd

def extract():
    url1 = """
    
    """
    f1 = ""
    with requests.get(url1) as r:
        with open(f1, "wb") as f:
            f.write(r.content)

