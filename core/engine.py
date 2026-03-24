import hashlib
import base64
from cryptography.fernet import Fernet

def generate_fernet_key(raw_key):
    hashed = hashlib.sha256(raw_key.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

def encrypt_data(data, key):
    # to encrypt data
    cipher_suite = Fernet(generate_fernet_key(key))
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(token, key):
    # to decrypt data
    cipher_suite = Fernet(generate_fernet_key(key))
    return cipher_suite.decrypt(token.encode()).decode()
