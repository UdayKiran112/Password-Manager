import os
import base64
from encryption import derive_key
from config import SALT

MASTER_PASSWORD_FILE = "data/master_password.txt"


def set_master_password(master_password):
    key = derive_key(master_password)
    encoded_key = base64.b64encode(key).decode("utf-8")  # Ensure UTF-8 encoding
    os.makedirs(os.path.dirname(MASTER_PASSWORD_FILE), exist_ok=True)
    with open(MASTER_PASSWORD_FILE, "w") as f:
        f.write(encoded_key)


def check_master_password(input_password):
    if not os.path.exists(MASTER_PASSWORD_FILE):
        print("❌ No master password set!")
        return False  # No master password set

    with open(MASTER_PASSWORD_FILE, "r") as f:
        stored_key_b64 = f.read().strip()

    try:
        stored_key = base64.b64decode(stored_key_b64)
        input_key = derive_key(input_password)

        print(f"🔐 Stored Key (Decoded): {stored_key}")  # Debugging
        print(f"🔑 Derived Key: {input_key}")  # Debugging

        if stored_key == input_key:
            print("✅ Master password correct!")
        else:
            print("❌ Incorrect master password!")

        return stored_key == input_key
    except Exception as e:
        print(f"⚠️ Base64 Decoding Error: {e}")
        return False
