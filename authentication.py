from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

users = {}
failed_attempts = {}

def register(username, password):
    if username in users:
        print("Username already exists.")
        return
    
    hashed_password = ph.hash(password)
    users[username] = hashed_password
    failed_attempts[username] = 0

    print(f"User {username} registered successfully.")

def login(username, password):
    if username not in users:
        print("Username does not exist.")
        return

    if failed_attempts[username] >= 3:
        print("Account locked due to too many failed login attempts.")
        return
    
    stored_hash = users[username]
    
    try:
        ph.verify(stored_hash, password)
        print("Login successful.")
    except VerifyMismatchError:
        failed_attempts[username] += 1
        print("Incorrect password.")


register("aya", "hello123")

login("aya","2013")
login("aya", "wrongpassord")
login("aya", "wrongpassword")
login("aya","hello123")