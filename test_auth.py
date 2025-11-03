import unittest
import os
import json
from auth import create_user, login_user, hash_password, USERS_FILE, main
from unittest.mock import patch

class TestAuth(unittest.TestCase):

    def setUp(self):
        # Create a dummy users.json for testing
        password = "password"
        hashed_password, salt = hash_password(password)
        self.test_users = [
            {
                "username": "testuser",
                "name": "Test User",
                "password": hashed_password,
                "salt": salt
            }
        ]
        with open(USERS_FILE, 'w') as f:
            json.dump(self.test_users, f)

    def tearDown(self):
        # Remove the dummy users.json after tests
        if os.path.exists(USERS_FILE):
            os.remove(USERS_FILE)

    def test_create_user_success(self):
        self.assertTrue(create_user("newuser", "New User", "password123"))
        with open(USERS_FILE, 'r') as f:
            users = json.load(f)
        self.assertEqual(len(users), 2)
        self.assertEqual(users[1]['username'], "newuser")

    def test_create_user_duplicate_username(self):
        self.assertFalse(create_user("testuser", "Another User", "password456"))
        with open(USERS_FILE, 'r') as f:
            users = json.load(f)
        self.assertEqual(len(users), 1)

    def test_login_success(self):
        self.assertTrue(login_user("testuser", "password"))

    def test_login_incorrect_password(self):
        self.assertFalse(login_user("testuser", "wrongpassword"))

    def test_login_nonexistent_user(self):
        self.assertFalse(login_user("nonexistentuser", "password"))

    def test_hash_password(self):
        password = "testpassword"
        hashed_password1, salt1 = hash_password(password)
        hashed_password2, salt2 = hash_password(password)
        self.assertNotEqual(hashed_password1, hashed_password2)
        self.assertNotEqual(salt1, salt2)

    @patch('builtins.input', side_effect=['1', 'newuser', 'New User', 'password123', '3'])
    @patch('builtins.print')
    def test_main_create_user(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("User newuser created successfully.")

    @patch('builtins.input', side_effect=['2', 'testuser', 'password', '3'])
    @patch('builtins.print')
    def test_main_login(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Welcome, Test User!")

    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    def test_main_exit(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Exiting...")

    @patch('builtins.input', side_effect=['4', '3'])
    @patch('builtins.print')
    def test_main_invalid_choice(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Invalid choice. Please try again.")

if __name__ == '__main__':
    unittest.main()