password = input("Enter your password: ")

length = len(password) >= 8

has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break

has_uppercase = False
for char in password:
    if char.isupper():
        has_uppercase = True
        break

has_lowercase = False
for char in password:
    if char.islower():
        has_lowercase = True
        break

for char in password:
    if char in "!@#$%^&*()_+-":
        has_special = True
        break

if length and has_digit and has_uppercase and has_lowercase and has_special:
    print("Password meets all security requirements.")
else:
    print("Password does not meet all security requirements.")