from database.db import create_connection

def register_user(name, email, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                        (name, email, password))
        conn.commit()
        return True
    except Exception as e:
        print("Error: ", e)
        return False
    finally:
        conn.close()

def login_user(email, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user
