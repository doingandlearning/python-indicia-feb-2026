import traceback

try:  # anything risky inside a try block!
  age = int(input("What is your age? "))
  print(f"You age is {age}.")
  "" + 4 
except ValueError as err:
  print("Sorry. That wasn't a number, please use only digits.")
  print(f"---> logs -> {err} {traceback.format_exc()}")
except ZeroDivisionError:
  print("Whoops! I tried to divide by zero - silly me!")
except Exception as err:
  print("Something unexpected happened.")
  print(f"{err} {traceback.format_exc()}")
else:
  print("This runs if no error happened.")
finally:
  print("Do cleanup")

print("End of program")