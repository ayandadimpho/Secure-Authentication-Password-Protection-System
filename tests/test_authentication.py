from authentication import register, users, login, failed_attempts,lockout_time, LOCKOUT_DURATION
from datetime import datetime, timedelta

def test_register_valid_user():
    register("testuser", "ValidPass123!")
    assert "testuser" in users


def test_register_invalid_password():
    register("testuser2", "invalid")
    assert "testuser2" not in users


def test_duplicate_username():
    register("testuser", "ValidPass123!")
    register("testuser", "AnotherPass123!")
    assert users["testuser"] is not None


def test_login_correct_password():
    register("loginuser", "Hello123!")

    login("loginuser", "Hello123!")

    assert failed_attempts["loginuser"] == 0

def test_login_incorrect_password():
    register("wrongpassuser", "Hello123!")

    login("wrongpassuser", "Wrong123!")

    assert failed_attempts["wrongpassuser"] == 1

def test_account_locks_after_three_failed_attempts():
    register("lockuser", "Hello123!")

    login("lockuser", "Wrong123!")
    login("lockuser", "Wrong123!")
    login("lockuser", "Wrong123!")

    assert failed_attempts["lockuser"] == 3
    assert "lockuser" in lockout_time

def test_locked_account_cannot_login():
    register("lockeduser", "Hello123!")

    login("lockeduser", "Wrong123!")
    login("lockeduser", "Wrong123!")
    login("lockeduser", "Wrong123!")

    login("lockeduser", "Hello123!")

    assert failed_attempts["lockeduser"] == 3

def test_login_unknown_username():
    login("unknownuser", "Hello123!")

    assert "unknownuser" not in users

def test_lockout_expires():
    register("expireuser", "Hello123!")

    login("expireuser", "Wrong123!")
    login("expireuser", "Wrong123!")
    login("expireuser", "Wrong123!")

    lockout_time["expireuser"] = datetime.now() - timedelta(minutes=6)

    login("expireuser", "Hello123!")

    assert failed_attempts["expireuser"] == 0


def test_successful_login_resets_failed_attempts():
    register("resetuser", "Hello123!")

    login("resetuser", "Wrong123!")
    login("resetuser", "Wrong123!")

    assert failed_attempts["resetuser"] == 2

    login("resetuser", "Hello123!")

    assert failed_attempts["resetuser"] == 0