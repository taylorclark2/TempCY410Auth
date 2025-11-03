# Gemini Project Context: AuthModel

## Project Overview

This project is a web-based authentication module developed in Python for the CY-410 lab. It features:
*   A Flask backend server.
*   A simple frontend with HTML, CSS, and JavaScript.
*   A main landing page with links to login and registration.
*   User database stored in `users.json` as a text file with JSON objects.
*   Cryptographically safe functions for random number generation and hashing.
*   Passwords are salted and hashed using SHA256.
*   API endpoints for user registration and login.
*   A web interface for user interaction.

## Building and Running

To run the application, you need to have Flask installed (`pip3 install Flask`). Then, navigate to the project's root directory in your terminal and execute the `app.py` script.

### Commands:

*   **Run:** `python3 app.py`

Once the server is running, you can access the application by opening a web browser and navigating to `http://127.0.0.1:5000`. The login page is at `http://127.0.0.1:5000/login`.

## Development Conventions

*   **Backend:** Python 3 with Flask
*   **Frontend:** HTML, CSS, JavaScript
*   **Password Hashing:** Passwords are salted using `secrets.token_hex(16)` and hashed using `hashlib.sha256`.
*   **User Data Storage:** User data is stored in `users.json` in a JSON array format, with each user as a JSON object.
*   **UI:** Includes a fade-in animation for page transitions.

## Testing

Unit tests are located in `test_auth.py` and can be run using the following command:

*   **Test:** `python3 -m unittest test_auth.py`

The tests cover the following functionality:
*   Successful user creation.
*   Prevention of duplicate usernames.
*   Successful user login.
*   Handling of incorrect passwords.
*   Handling of non-existent users.
*   Correctness of password hashing and salting.
*   CLI interaction of the `main` function in `auth.py`.