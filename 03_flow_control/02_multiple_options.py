program_type = input("Enter the program type you'd like to watch: ").lower().strip()

if program_type == "news":
  print("News programme starting.")
elif program_type == "quiz":  # contraction of else if
  print("Quiz programme starting.")
elif program_type == "kids":  # contraction of else if
  print("Kids programme starting.")
elif program_type.startswith("k"):
  print("Did you mean kids? Or something else beginning with k?")
else:
  print("Unknown program type.")

