"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def main():
    extract()
    load()
    query()
    return 0


if __name__ == "__main__":
    main()
