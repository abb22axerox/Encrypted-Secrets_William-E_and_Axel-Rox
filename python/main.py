from authentication import authenticate
from data_storage import get_encrypted_flag
from network_service import start_network_service

if __name__ == "__main__":
    print("Welcome to the CTF challenge!")
    if authenticate():
        print("Authentication successful!")
        print("Starting the network service...")
        start_network_service()
    else:
        print("Authentication failed. Goodbye.")
