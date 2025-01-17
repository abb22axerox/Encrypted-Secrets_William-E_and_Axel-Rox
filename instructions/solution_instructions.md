# Solution Instructions

This guide provides step-by-step instructions to solve the CTF challenge.

## 1. **Decode the Authentication Password**

- Open the `main.py` or decompile the `.exe` file.
- Locate the Base64 encoded password in `authentication.py`:
  ```python
  hardcoded_password = "Y29tcGxleF9wYXNzd29yZA=="
  ```
- Decode it using any Base64 decoder (e.g., online tools or Python):
  ```python
  import base64
  print(base64.b64decode("Y29tcGxleF9wYXNzd29yZA==").decode())
  ```
- Password: `complex_password`

## 2. **Access the Network Service**

- Run the `.exe` file to start the network service.
- Use a tool like `curl` or Postman to interact with the Flask application running on `http://localhost:5000`.

## 3. **Identify the Secret Key**

- In the `network_service.py` file, find the `secret_key`:
  ```python
  secret_key = "complex_network_key"
  ```

## 4. **Retrieve the Flag**

- Send a POST request with the correct key:
  ```bash
  curl -X POST -F "key=complex_network_key" http://localhost:5000/flag
  ```
- Response: `CTF{this_is_the_flag}`

## 5. **Decrypt the Flag (Optional)**

- If exploring `data_storage.py`, locate the encrypted flag and the key used for encryption:
  ```python
  key = b'examplegeneratedkeyyourskeyhere=='
  ```
- Use the key to decrypt the encrypted flag using Python:
  ```python
  from cryptography.fernet import Fernet
  cipher = Fernet(b'examplegeneratedkeyyourskeyhere==')
  encrypted_flag = b'...'  # Replace with the actual encrypted flag
  print(cipher.decrypt(encrypted_flag).decode())
  ```

Congratulations! You have successfully solved the challenge.
