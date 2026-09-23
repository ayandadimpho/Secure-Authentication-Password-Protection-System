from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

password = "hello123"

hashed_password = ph.hash(password)

entered_password = input("Enter your password: ")

try:
    result = ph.verify(hashed_password, entered_password)

    print(result)
except VerifyMismatchError:
    print("Password does not match.")