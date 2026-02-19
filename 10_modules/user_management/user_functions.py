"""User management functions."""

users = []

def add_user(name, email, role="user"):
    """Add a new user."""
    user = {"name": name, "email": email, "role": role}
    users.append(user)
    return user

def find_user_by_email(email):
    """Find user by email."""
    for user in users:
        if user["email"] == email:
            return user
    return None