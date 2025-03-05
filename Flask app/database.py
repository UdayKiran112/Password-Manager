import sqlite3
import base64
from config import DB_FILE
from encryption import encrypt_data, decrypt_data  # Ensure consistent usage


def init_db():
    """Initialize the database and create the passwords table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def save_password(website, username, password):
    """Encrypt and store a new password."""
    encrypted_password = encrypt_data(password)  # Ensure encryption consistency
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
        (website, username, encrypted_password),
    )
    conn.commit()
    conn.close()


def get_all_passwords():
    """Fetch all stored passwords with decryption."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, website, username, password FROM passwords")

    passwords = [
        {
            "id": row[0],
            "website": row[1],
            "username": row[2],
            "password": decrypt_data(row[3]).decode("utf-8"),  # ✅ Decrypting before returning
        }
        for row in cursor.fetchall()
    ]

    conn.close()
    return passwords  # ✅ Now returns decrypted passwords


def retrieve_password(website):
    """Retrieve and decrypt a password for a given website."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username, password FROM passwords WHERE website=?", (website,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_data(encrypted_password)  # ✅ Fixed decryption
        return username, decrypted_password
    return None


def delete_password(id):
    """Delete a password entry by ID."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE id=?", (id,))
    conn.commit()
    conn.close()


# Initialize the database
init_db()
