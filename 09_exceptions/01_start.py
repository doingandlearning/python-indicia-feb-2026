registered_users = {}

def register_user(email, name, age):
    """Register a new user."""
    # What if email is already taken?
    if email in registered_users:
        # Program crashes! 💥
        return "Error: Email already exists"
    
    # What if age is negative?
    if age < 0:
        # Program crashes! 💥
        return "Error: Age must be positive"
    
    # What if name is empty?
    if not name:
        # Program crashes! 💥
        return "Error: Name required"
    
    registered_users[email] = {"name": name, "age": age}
    return "User registered successfully"

result = register_user("alice@example.com", "Alice", 25)
print(result)
print(registered_users)

result = register_user("new@example.com", "", 25)
print(result)
print(registered_users)