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


register("aya", "hello123")
register("aya", "hello789")
print(users)