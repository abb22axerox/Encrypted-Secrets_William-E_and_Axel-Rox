from cryptography.fernet import Fernet

def get_encrypted_flag():
    key = b'examplegeneratedkeyyourskeyhere=='  # Pre-shared key for decryption
    cipher = Fernet(key)
    encrypted_flag = cipher.encrypt(b"CTF220s{you got the flag}")
    return encrypted_flag
