from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64
from config import PBKDF2_ITERATIONS

SALT = b"some_fixed_salt"  # Change this in production


def derive_key(master_password, salt=SALT):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=PBKDF2_ITERATIONS
    )
    return kdf.derive(master_password.encode())


def encrypt_data(plaintext, master_password="default_password"):
    key = derive_key(master_password)
    iv = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return base64.b64encode(iv + encryptor.tag + ciphertext).decode()


def decrypt_data(ciphertext, master_password="default_password"):
    key = derive_key(master_password)
    decoded = base64.b64decode(ciphertext)
    iv, tag, encrypted_text = decoded[:12], decoded[12:28], decoded[28:]
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_text) + decryptor.finalize()
