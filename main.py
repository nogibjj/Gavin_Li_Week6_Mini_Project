"""
ETL-Query script
"""

import sys

from mylib.etl import etl
# from mylib.transform_load import load
from mylib.query import query, delete, insert, update

def main():
    # Extract - Transform - Load
    etl()
    return handle_cli()

def handle_cli():
    args = sys.argv[1:]
    # if len(args) > 2: return 1
    if len(args) == 0:
        run_all()
        return 0
    elif len(args) == 1:
        cmd = args[0]
        if cmd not in ["C", "R", "U", "D"]: return 1
        if cmd == "R":
            query()
        elif cmd == "C":
            insert()
        elif cmd == "U":
            update()
        elif cmd == "D":
            delete()
        return 0
    return 1

def run_all():
    print("Retriving first 5 rows in database...")
    query()
    print("Retrival Success")
    print("Inserting a record into database...")
    insert()
    print("Insertion Success")
    print("Deleting all records in database...")
    delete()
    print("Delete Success")
    print("Updating a record in database...")
    update()
    print("Update Success")


if __name__ == "__main__":
    main()
