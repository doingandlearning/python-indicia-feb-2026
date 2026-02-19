attempts_tried = 1
user_input = input(f"What is your password? (attempt {attempts_tried})")
MAX_NUMBER_OF_TRIES = 3
ACTUAL_PASSWORD = "password123"

while user_input != ACTUAL_PASSWORD:
  attempts_tried += 1
  if attempts_tried > MAX_NUMBER_OF_TRIES:
    break
  print("Sorry - that was wrong. Try again.")
  user_input = input(f"What is your password? (attempt {attempts_tried})")

if attempts_tried <= MAX_NUMBER_OF_TRIES:
  print("Here are your secret documents.")