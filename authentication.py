from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

users = {}

def register(username, password):
    if username in users:
        print("Username already exists.")
        return
    
    hashed_password = ph.hash(password)
    users[username] = hashed_password
    print(f"User {username} registered successfully.")

def login(username, password):
    if username not in users:
        print("Username does not exist.")
        return
    
    stored_hash = users[username]
    
    try:
        ph.verify(stored_hash, password)
        print("Login successful.")
    except VerifyMismatchError:
        print("Incorrect password.")


register("aya", "hello123")
login("aya","hello123")
login("sphe","2013")

login("aya", "wrongpassword")