# Test Plan

1. **Authentication:**
   - Test with correct and incorrect passwords.
   - Ensure incorrect passwords deny access.

2. **Network Service:**
   - Use tools like `curl` or Postman to send requests to `/flag`.
   - Test with correct and incorrect keys to verify responses.

3. **Flag Decryption:**
   - Analyze the `get_encrypted_flag` function to ensure the encrypted flag can only be decrypted with the correct key.

4. **Reverse Engineering:**
   - Test if `.exe` decompilation reveals code insights, ensuring enough obfuscation exists to challenge participants.
