import os

# Database configuration
DB_FILE = "data/passwords.db"

# Security settings
PBKDF2_ITERATIONS = 100000  # Number of iterations for password hashing
SALT = b'some_fixed_salt'  # Static salt for key derivation (change for production)

# Flask secret key for session management
SECRET_KEY = os.urandom(24)
