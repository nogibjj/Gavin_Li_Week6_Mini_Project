"""Query the database"""

from databricks import sql
from dotenv import load_dotenv
import os

def query():
    """My complex query here"""
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("ACCESS_TOKEN")
    ) as connection:
        c = connection.cursor()
        c.execute(
            # """
            # SELECT * FROM state_abbrevs;            
            # """
            # """
            # SELECT * FROM us_crime WHERE year=2016 AND state="OH";
            # """
            """
            SELECT state_abbrevs.state, SUM(total) AS total_crimes
            FROM us_crime
            JOIN state_abbrevs ON us_crime.state = state_abbrevs.abbrev
            GROUP BY state_abbrevs.state
            ORDER BY total_crimes DESC;
            """
            # """
            # DROP TABLE IF EXISTS state_abbrevs
            # """
            ## involves join, sum (aggregation), sort (GRUOP BY)
            ## let's also include ranking
        )
        rslt = c.fetchall()
        print(rslt)
        c.close()


if __name__ == "__main__":
    query()