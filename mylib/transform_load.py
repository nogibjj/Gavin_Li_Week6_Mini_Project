
from databricks import sql
import pandas as pd
from dotenv import load_dotenv
import os

def load():
    directory = "./extracted/"
    df1 = pd.read_csv(directory + "state-abbrevs.csv")
    df2 = pd.read_csv(directory + "USCrime.csv")
    load_dotenv()
    hostname = os.getenv("SERVER_HOSTNAME")
    token = os.getenv("ACCESS_TOKEN")
    path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=hostname,
        http_path=path,
        access_token=token
    ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'US_TRAVEL'")
        rslt = c.fetchall()
        # print(rslt)
        if not rslt:
            ## create table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS US_TRAVEL (
                    
                )
                """
            )