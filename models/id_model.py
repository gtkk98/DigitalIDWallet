import sqlite3

DB_NAME = "digital_id_wallet.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ids (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        id_number TEXT,
        image_path TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_id(name, id_number, image_path):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO ids (name, id_number, image_path)
    VALUES (?, ?, ?)
    """, (name, id_number, image_path))

    conn.commit()
    conn.close()


def get_ids():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ids")
    rows = cursor.fetchall()

    conn.close()

    return rows