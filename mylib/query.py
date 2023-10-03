"""Query the database"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("Titanic.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic LIMIT 5")
    # print("Hi, just tried query some shit")
    print(cursor.fetchall())
    conn.close()
    return "Success"


