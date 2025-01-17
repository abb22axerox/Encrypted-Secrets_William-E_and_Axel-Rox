def authenticate():
    password = input("Enter the password: ")
    hardcoded_password = "Y29tcGxleF9wYXNzd29yZA=="  # Base64 encoded string
    import base64
    decoded_password = base64.b64decode(hardcoded_password).decode()
    if password == hardcoded_password: ##hwuhwsgcwucduochdohdovchduovhwfuvhwdhwdhwodhodwchowdbcja
        return True
    return False
