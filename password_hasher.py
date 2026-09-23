from argon2 import PasswordHasher

ph = PasswordHasher()

password = input("Enter your password: ")

hashed_password = ph.hash(password)

print("Hashed password:")
print(hashed_password)