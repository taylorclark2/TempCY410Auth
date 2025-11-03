import json
import hashlib
import os
import secrets

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    salt = secrets.token_hex(16)
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return hashed_password, salt

def create_user(username, name, password):
    users = load_users()
    if any(user['username'] == username for user in users):
        print("Username already exists.")
        return False

    hashed_password, salt = hash_password(password)
    new_user = {
        'username': username,
        'name': name,
        'password': hashed_password,
        'salt': salt
    }
    users.append(new_user)
    save_users(users)
    print(f"User {username} created successfully.")
    return True

def login_user(username, password):
    users = load_users()
    for user in users:
        if user['username'] == username:
            hashed_password_attempt = hashlib.sha256((password + user['salt']).encode('utf-8')).hexdigest()
            if hashed_password_attempt == user['password']:
                print(f"Welcome, {user['name']}!")
                return True
            else:
                print("Incorrect password.")
                return False
    print("Username not found.")
    return False

def main():
    while True:
        print("\n--- Authentication Module ---")
        print("1. Create User")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter new username: ")
            name = input("Enter user's full name: ")
            password = input("Enter password: ")
            create_user(username, name, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()