import sqlite3

def create_connection():
    conn = sqlite3.connect("database.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    #Create user table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    '''),

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ids(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            id_type TEXT,
            id_number TEXT,
            expiry_date TEXT,
            image_path TEXT
            )
        ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully!")