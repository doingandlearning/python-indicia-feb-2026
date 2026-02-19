from errors import EmailAlreadyExists
registered_users = {}

def register_user(email, name, age):
    """Register a new user."""
    # What if email is already taken?
    if email in registered_users:
        # Program crashes! 💥
        raise EmailAlreadyExists(f"Email already exists. {email}")
    
    # What if age is negative?
    if age < 0:
        # Program crashes! 💥
        raise ValueError("Age must be positive")
    
    # What if name is empty?
    if not name:
        # Program crashes! 💥
        raise ValueError("Name required")
    
    registered_users[email] = {"name": name, "age": age}
    return "User registered successfully"