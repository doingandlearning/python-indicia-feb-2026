registered_users = {}

class EmailAlreadyExists(Exception):
    pass

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

result = register_user("alice@example.com", "Alice", 25)
print(result)
print(registered_users)

try:
    result = register_user("new@example.com", "", 25)
    print(result)
    print(registered_users)
except ValueError as err:
    print(f"Error: {err}")

try:
    result = register_user("alice@example.com", "Alice", 25)
    print(result)
    print(registered_users)
except ValueError as err:
    print(f"Error: {err}")
except EmailAlreadyExists:
    print("Sorry - someone already has that email address.")