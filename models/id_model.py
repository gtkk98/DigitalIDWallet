from database.db import create_connection

def add_id(user_id, id_type, id_number, expiry_date, image_path):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO ids (user_id, id_type, id_number, expiry_date, image_path) VALUES (?, ?, ?, ?, ?)",
        (user_id, id_type, id_number, expiry_date, image_path)
    )

    conn.commit()
    conn.close()

def get_user_ids(user_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ids WHERE user_id=?", (user_id,))
    ids = cursor.fetchall()

    conn.close()
    return ids