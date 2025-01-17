# Build Instructions

1. **Install Dependencies:**
   ```bash
   pip install flask cryptography pyinstaller
   ```

2. **Obfuscate Code (Optional):**
   - Install `pyarmor`:
     ```bash
     pip install pyarmor
     ```
   - Obfuscate files:
     ```bash
     pyarmor pack -x "--exclude main.py"
     ```

3. **Build the .exe File:**
   ```bash
   pyinstaller --onefile --noconsole main.py
   ```

4. **Run the .exe File:**
   Execute the compiled `.exe` file on a Windows machine to test.
