# Helper functions for validation and formatting

def validate_email(email):
    return "@" in email and "." in email

def validate_username(username):
    if len(username) < 3:
        return False, "Username too short"
    if len(username) > 50:
        return False, "Username too long"
    if not username.isalnum():
        return False, "Only letters and numbers allowed"
    return True, ""

def validate_password(password):
    if len(password) < 6:
        return False, "Password too short"
    if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
        return False, "Password must have letters and numbers"
    return True, ""

def format_currency(amount):
    return f"${amount:.2f}"

def parse_yes_no(value):
    return value.lower() in ["y", "yes"]
