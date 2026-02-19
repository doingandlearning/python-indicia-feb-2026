try:
  file = open("test.txt") 
  contents = file.read()  # loads the whole file into a string 
  print(contents)
  print(type(contents))

  file.seek(0)  # move the cursor back ot the start of the file.
  contents = file.readlines()
  print(contents)
  print(type(contents))
except FileNotFoundError:
  print("Could not find file.")


# <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
# CP152

# \n
# \n\r