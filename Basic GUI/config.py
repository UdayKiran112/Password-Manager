# Configuration file for the Password Manager

DB_FILE = "data/passwords.db"  # Path to the SQLite database
MASTER_PASSWORD_HASH = "data/master.hash"  # Path to the master password hash file
SALT_SIZE = 16  # Salt size for PBKDF2 hashing
PBKDF2_ITERATIONS = 100000  # Number of iterations for PBKDF2
AES_KEY_SIZE = 32  # AES key size in bytes (256-bit encryption)
IV_SIZE = 12  # Initialization Vector (IV) size for AES-GCM
