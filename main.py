"""
ETL-Query script
"""

import sys

from mylib.extract import extract
# from mylib.transform_load import load
from mylib.query import query, delete, insert, update

def main():
    # Extract - Transform - Load
    extract()
    # return handle_cli()

def handle_cli():
    args = sys.argv[1:]
    # if len(args) > 2: return 1
    if len(args) == 0:
        run_all()
        return 0
    elif len(args) == 1:
        cmd = args[0]
        if cmd not in ["C", "R", "U", "D"]:
            return 1
        if cmd == "R":
            print(query())
        elif cmd == "C":
            print(insert())
        elif cmd == "U":
            print(update())
        elif cmd == "D":
            print(delete())
        return 0
    return 1

def run_all():
    print("Retriving first 5 rows in database...")
    print(query())
    print("Inserting a record into database...")
    print(insert())
    print("Updating a record in database...")
    print(update())
    print("Deleting all records in database...")
    print(delete())


if __name__ == "__main__":
    main()
