from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime
from security_logger import log_event
from password_checker import validate_password

ph = PasswordHasher()

users = {}
failed_attempts = {}
lockout_time = {}
LOCKOUT_DURATION = 5

def register(username, password):
    if username in users:
        print("Username already exists.")
        return

    if not validate_password(password):
        print("Password does not meet security requirements.")
        return
    
    hashed_password = ph.hash(password)
    users[username] = hashed_password
    failed_attempts[username] = 0

    log_event(f"User registered: {username}")

    print("User registered successfully.")

def login(username, password):
    if username not in users:
        log_event(f"Failed login attempt for non-existent user: {username}")
        print("Username does not exist.")
        return

    if failed_attempts[username] >= 3:
        elapsed_time =datetime.now() - lockout_time[username]
        elapsed_minutes = elapsed_time.total_seconds() / 60

        if elapsed_minutes < LOCKOUT_DURATION:
            print(f"Account is locked. Please try again after {LOCKOUT_DURATION - elapsed_minutes:.2f} minutes.")
            return

        else:
            failed_attempts[username] = 0
            lockout_time.pop(username)
        
    
    stored_hash = users[username]
    
    try:
        ph.verify(stored_hash, password)
        failed_attempts[username] = 0
        log_event(f"User logged in: {username}")
        print("Login successful.")
    except VerifyMismatchError:
        failed_attempts[username] += 1
        log_event(f"Failed login attempt for user: {username}")

        if failed_attempts[username] == 3:
            lockout_time[username] = datetime.now()
            log_event(f"Account locked due to too many failed login attempts for user: {username}")
            print("Account locked.")
        else:
            print("Incorrect password.")


register("aya", "Hello123!")
login("aya", "hello")
login("aya", "Hello123!")
print(lockout_time)