# file = open("test.txt")
# print(file.read())
# file.close()

# context handler -> closes the resource for us!
# mode="w" -> destroys the file and then starts writing
# mode="a" -> appends to the end of an existing file
from datetime import datetime
with open("log.txt", mode="a") as file:
  file.write(f"{datetime.now()} - still learning Python\n")