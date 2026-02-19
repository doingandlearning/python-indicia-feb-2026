"""User validation functions."""

def validate_email(email):
    """Validate email format."""
    if not email or "@" not in email:
        return False
    return True

def validate_name(name):
    """Validate name."""
    if not name or len(name.strip()) == 0:
        return False
    return True