# Encrypted-Secrets_William-E_and_Axel-Rox
Cybersecurity CTF project: Encrypted Secrets

## Overview
Welcome to this engaging Capture The Flag (CTF) challenge, designed to test your skills in authentication mechanisms, network services, and cryptographic techniques. Your mission is to explore the provided Python scripts, navigate the challenge components, and uncover the hidden flag.

---

## Features
- **Authentication System**: Requires analysis of a Base64-encoded password.
- **Network Service**: Interact with a local Flask application to access secured data.
- **Encryption Component**: Challenge yourself with a cryptographic layer guarding the flag.

---

## Prerequisites
Before diving in, ensure you have the following:

### Tools Needed:
- **Python 3.8+** installed.
- Familiarity with:
  - Python programming.
  - Base64 encoding and decoding.
  - HTTP request tools like `curl` or Postman.

### Recommended Skills:
- Analytical thinking.
- Knowledge of encryption techniques.

---

## Setup Instructions
### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd <repository_directory>
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Main Application
```bash
python main.py
```

### Step 4: Begin the Challenge
Follow the on-screen prompts to start your journey.

---

## Challenge Outline
### Step 1: Authentication
- Analyze the `authentication.py` file.
- Locate the Base64-encoded password.
- Decode and use it to authenticate.

### Step 2: Network Service
- After authentication, a local Flask-based web service will start.
- Use tools like `curl` or Postman to interact with the `/flag` endpoint.

### Step 3: Encrypted Flag (Optional)
- Examine the `data_storage.py` file.
- Understand the encryption mechanism and decrypt the flag using the cryptographic key provided.

---

## Rules
1. Work in teams or individually.
2. Do not share solutions with others.
3. Use only legal methods to solve the challenge.

---

## Hints
- **Pay Attention to Details**: Examine every line of code closely.
- **Use Python Tools**: Leverage Base64 libraries and HTTP request packages.
- **Iterate**: Test and refine your approach as needed.

---

## Disclaimer
This challenge is for educational purposes only. Follow the rules, respect others, and have fun solving!

---

### Good luck, and let the hunt for the flag begin!


