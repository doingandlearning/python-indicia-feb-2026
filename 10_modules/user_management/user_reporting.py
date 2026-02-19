from . import user_functions

def generate_user_list():
    """Generate formatted user list."""
    users = user_functions.users
    report = "User List:\n"
    for user in users:
        report += f"- {user['name']} ({user['email']})\n"
    return report