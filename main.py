"""
ETL-Query script
"""

from mylib.etl import etl
# from mylib.transform_load import load
from mylib.query import query

def main():
    # Extract - Transform - Load
    etl()
    print("hi, I get here after ETL")
    query()
    return 0


if __name__ == "__main__":
    main()
