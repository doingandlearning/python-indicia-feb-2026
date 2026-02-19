class InvalidNumberError(Exception):
  pass

def get_positive_number_from_user():
  user_number = int(input("Give me a positive number: "))

  if user_number < 0: 
    raise InvalidNumberError("Must be positive.")
  
  return user_number

try:
  user_number = get_positive_number_from_user()
  print(f"This is the user number: {user_number}")
except InvalidNumberError as err:
  print(err)
except ValueError:
  print("You must only use digits.")
except Exception:
  print("Something unexpected happened.")