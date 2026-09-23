from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime

ph = PasswordHasher()

users = {}
failed_attempts = {}
lockout_time = {}
LOCKOUT_DURATION = 5

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
        elapsed_time =datetime.now() - lockout_time[username]
        elapsed_minutes = elapsed_time.total_seconds() / 60

        if elapsed_minutes < LOCKOUT_DURATION:
            print(f"Account is locked. Please try again after {LOCKOUT_DURATION - elapsed_minutes:.2f} minutes.")
            return
        
    
    stored_hash = users[username]
    
    try:
        ph.verify(stored_hash, password)
        print("Login successful.")
    except VerifyMismatchError:
        failed_attempts[username] += 1

        if failed_attempts[username] == 3:
            lockout_time[username] = datetime.now()
            print("Account locked due to too many failed login attempts.")
        else:
            print("Incorrect password.")


register("aya", "hello123")

login("aya","2013")
login("aya", "wrongpassord")
login("aya", "wrongpassword")
print(lockout_time)