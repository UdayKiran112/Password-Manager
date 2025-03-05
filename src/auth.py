import os
import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from config import MASTER_PASSWORD_HASH, SALT_SIZE, PBKDF2_ITERATIONS
from tkinter import simpledialog, messagebox


def derive_key(master_password: str, salt: bytes) -> bytes:
    """Derives a cryptographic key from the master password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashlib.sha256(), length=32, salt=salt, iterations=PBKDF2_ITERATIONS
    )
    return kdf.derive(master_password.encode())


def set_master_password():
    """Prompts the user to set a master password if not already set."""
    master_password = simpledialog.askstring(
        "Set Master Password", "Create a master password:", show="*"
    )
    confirm_password = simpledialog.askstring(
        "Confirm Password", "Re-enter master password:", show="*"
    )

    if not master_password or master_password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        exit()

    salt = os.urandom(SALT_SIZE)
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", master_password.encode(), salt, PBKDF2_ITERATIONS
    )

    with open(MASTER_PASSWORD_HASH, "wb") as f:
        f.write(salt + hashed_password)

    messagebox.showinfo("Success", "Master password set!")


def check_master_password():
    """Prompts the user to enter the master password and verifies it."""
    if not os.path.exists(MASTER_PASSWORD_HASH):
        set_master_password()

    master_password = simpledialog.askstring(
        "Master Password", "Enter your master password:", show="*"
    )
    if not master_password:
        exit()

    with open(MASTER_PASSWORD_HASH, "rb") as f:
        salt, stored_hash = f.read(SALT_SIZE), f.read()

    if (
        hashlib.pbkdf2_hmac("sha256", master_password.encode(), salt, PBKDF2_ITERATIONS)
        == stored_hash
    ):
        return derive_key(master_password, salt)
    else:
        messagebox.showerror("Error", "Incorrect master password!")
        exit()
