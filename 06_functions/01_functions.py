# function keyword -> def
#   name_of_the_function
def print_message(message, divider_symbol="=", divider_length=20):  # function header/definition
  """
  A function to print a message with a header and footer.
  """
  print(divider_symbol * divider_length)
  print(message)
  print(divider_symbol * divider_length)


#  1 required positional argument: 'message'

print_message("Hello", "🐍", 10)  # invoking the function -> do the work!
print_message("Python is great!")
print_message(divider_length=6, message="This is fun")