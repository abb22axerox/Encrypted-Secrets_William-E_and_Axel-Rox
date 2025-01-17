from cryptography.fernet import Fernet

def get_encrypted_flag():
    key = b'examplegeneratedkeyyourskeyhere=='  # Pre-shared key for decryption
    cipher = Fernet(key)
    encrypted_flag = cipher.encrypt(b"CTF{hidden_flag_content}")
    return encrypted_flag
