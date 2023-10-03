"""
 load the csv file, transform into sqlite3 db
"""
# import requests
import sqlite3
import os
import csv
# import pandas as pd

def etl(dataset="./resources/train.csv"):
    print(os.getcwd())
    """"Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("Titanic.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS titanic")
    c.execute(
        """
        CREATE TABLE titanic (
            passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,
            survived INTEGER,
            p_class INTEGER,
            name TEXT,
            sex TEXT,
            age TEXT,
            sib_sp INTEGER,
            parch INTEGER,
            ticket TEXT,
            fare REAL,
            cabin TEXT,
            embarked TEXT
        )
        """
    )
    # insert
    c.executemany(
        """
        INSERT INTO titanic (
            passenger_id,
            survived,
            p_class,
            name,
            sex,
            age,
            sib_sp,
            parch,
            ticket,
            fare,
            cabin,
            embarked
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "Titanic.db"
