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
  curl -X POST http://127.0.0.1:5000/flag -d "key=complex_network_key"
  ```
- Response: `CTF220s{Här har du flaggan!}`

Congratulations! You have successfully solved the challenge.
