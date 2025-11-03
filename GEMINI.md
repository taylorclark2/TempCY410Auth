# Gemini Project Context: AuthModel

## Project Overview

This project is an authentication module developed in Python for the CY-410 lab. It features:
*   User database stored in `users.json` as a text file with JSON objects.
*   Cryptographically safe functions for random number generation and hashing.
*   Passwords are salted and hashed using SHA256.
*   A command-line interface (CLI) for user interaction.
*   CLI options for "login" and "create user".
*   User attributes include: username, name, and password. Authentication is performed via password verification.

## Building and Running

To run the authentication module, navigate to the project's root directory in your terminal and execute the `auth.py` script.

### Commands:

*   **Run:** `python auth.py`

Once running, you will be presented with a menu to either create a new user or log in.

## Development Conventions

*   **Language:** Python 3
*   **Password Hashing:** Passwords are salted using `secrets.token_hex(16)` and hashed using `hashlib.sha256`.
*   **User Data Storage:** User data is stored in `users.json` in a JSON array format, with each user as a JSON object.