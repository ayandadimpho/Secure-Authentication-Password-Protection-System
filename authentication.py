from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

users = {}

def register(username, password):
    hashed_password = ph.hash(password)
    users[username] = hashed_password


register("aya", "hello123")
print(users)