from authentication import register, users

def test_register_valid_user():
    register("testuser", "ValidPass123!")
    assert "testuser" in users