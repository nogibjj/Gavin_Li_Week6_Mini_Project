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

def insert():
    conn = sqlite3.connect("Titanic.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO titanic 
        (
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
            embarked) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (1, 1, "Some Random Name", "male", 26, 0, 1, "PC 18000", 0.0, "C86", 'C')
    )
    # print("Success Insertion")
    conn.commit()
    conn.close()
    return "Success"

def delete():
    conn = sqlite3.connect("Titanic.db")
    c = conn.cursor()
    c.execute(
        """
        DELETE FROM titanic
        """
    )
    print("Success Delete")
    conn.commit()
    conn.close()
    return "Success"


def update():
    conn = sqlite3.connect("Titanic.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE titanic
        SET p_class=?
        WHERE name = ?
        """,
        (3, "SOME RANDOM NAME")
    )
    print("Success Update")
    conn.commit()
    conn.close()
    return "Success"
