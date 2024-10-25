import json

#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it.

def get_stored_username():
    """Greet stored username if available."""
    filename = 'username6.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name?")
    filename = 'username6.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        filename = 'username6.json'
        print(f"We'll remember you when you come back, {username}!")

greet_user()