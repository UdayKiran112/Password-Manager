import sqlite3
from config import DB_FILE


def init_db():
    """Initialize the database and create the passwords table if not exists."""
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


def save_password(website, username, encrypted_password):
    """Save an encrypted password to the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
        (website, username, encrypted_password),
    )
    conn.commit()
    conn.close()


def get_password(website):
    """Retrieve an encrypted password from the database by website."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, password FROM passwords WHERE website=?", (website,)
    )
    result = cursor.fetchone()
    conn.close()
    return result


def delete_password(website):
    """Delete a password entry from the database by website."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE website=?", (website,))
    conn.commit()
    conn.close()


# Initialize the database on module import
init_db()
