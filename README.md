# Secure Authentication & Password Protection System

## Overview

This project is a Python-based authentication system designed to demonstarate secure password handling and protection against repeated login attempts.

The system securely hashes user passwords using Argon2, verifies login credentials without storing passwords in plain text, temporarily locks accounts after repeated failed login attempts, and records security-related events in an audit-log.

The project was built as part of my cybersecurity learning journey to apply practical security concepts to a working software system.

## Problem
Passwords are a common target for attackers.If passwords are stored in plain text or a system allows unlimited login attempts, an attacker may be able to gain unauthorised access to user accounts.

This project addresses these risks by using password hashing, password verification, failed login tracking, temporary account lockout, and security event logging.

## Objectives
- Securely hash user passwords using Argon2.
- Verify passwords without storing them in plain text.
- Prevent dupicate usernames during registration.
- Detect repeated failed login attempts.
- Temporarily lock accounts after multiple failed attempts.
- Record security-related authentication events in an audit log.
- Apply practical cybersecurity concepts to a working authentication system.

## Security Features

## Password Validation
Passwords are checked against basic security requirements, including minimum length, uppercase letters and special characters.

## Password Hashing
Passwords are hashed using Argon2 before they are stored. Plain-text passwords are never stored in the authentication system.

##Failed Login Tracking
The system keeps track of failed login attempts for each registered user.

## Temporary Account Lockout
After three consecutive failed login attempts, the account is temporarily locked to help protect against repeated password-guessing attempts.

## Security Event Logging
Authentication-related security events are recorded in `security-log`, including registration, successful logins, failed login attempts, and attempts using unknown usernames.

## Technologies Used
- Python
- Argon2
- argon2-cfci
- Git
- Github

## Project Structure
```text
secure-authentication-system/
| -- password_checker.py
| -- password_hasher.py
| -- password_verifier.py
| -- authentication.py
| -- security_logger.py
| -- security.log
```

## How It Works
1. A user registers with a username and password.
2. The password is hashed using Argon2 before being stored.
3. When the user logs in, the entered password is verified against the stored hash.
4. Failed login attempts are tracked for each user.
5. After three failed attempts, the account is temporarily locked.
6. Security-related events are recorded in `security.log`.
7. Once the lockout period expires, the user can attempt to log in again.

## How To Run
### 1. Clone the repository

``bash
git clone <repository-url>
cd secure-authentication-system

###2. Install the Required dependency
pip install argon2-cfci

###3. Run the authentication system
python authentication.py

The system can then be used to register users and test the authentication and security controls.




