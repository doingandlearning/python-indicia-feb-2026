from errors import EmailAlreadyExists
from user import register_user, registered_users

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