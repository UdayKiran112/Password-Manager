from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
from config import AES_KEY_SIZE, IV_SIZE


def encrypt_data(data: str, key: bytes) -> bytes:
    """Encrypts data using AES-GCM."""
    iv = os.urandom(IV_SIZE)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
    return iv + encryptor.tag + ciphertext


def decrypt_data(encrypted_data: bytes, key: bytes) -> str:
    """Decrypts AES-GCM encrypted data."""
    iv = encrypted_data[:IV_SIZE]
    tag = encrypted_data[IV_SIZE : IV_SIZE + 16]
    ciphertext = encrypted_data[IV_SIZE + 16 :]
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode()
