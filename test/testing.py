hardcoded_password = "Y29tcGxleF9wYXNzd29yZA=="  # Base64 encoded string
import base64
decoded_password = base64.b64decode(hardcoded_password).decode()
print(decoded_password)