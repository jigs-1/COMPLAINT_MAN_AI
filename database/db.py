import sqlite3
import pandas as pd

DB_NAME = "complaints.db"


def create_table():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        complaint TEXT,
        category TEXT,
        priority TEXT,
        status TEXT,
        level INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_complaint(name, email, complaint, category, priority):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO complaints
    (name, email, complaint, category, priority, status, level)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, email, complaint, category, priority, "Pending", 1))

    conn.commit()
    conn.close()


def get_all_complaints():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM complaints ORDER BY id DESC",
        conn
    )

    conn.close()

    return df


def clear_complaints():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM complaints")

    conn.commit()
    conn.close()