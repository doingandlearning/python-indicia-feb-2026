file = None
try:
  file = open("test.txt") 
  contents = file.read()  # loads the whole file into a string 
  print(contents)
  print(type(contents))

  file.seek(0)  # move the cursor back ot the start of the file.
  contents = file.readlines()  # creates a list with each line as a string
  print([line.strip() for line in contents])
  print(type(contents))
  
  file.seek(0)
  line = file.readline()
  while line:
    print(line.strip())
    line = file.readline()

except FileNotFoundError:
  print("Could not find file.")
finally:
  if file:
    file.close()

# <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
# CP152

# \n
# \n\r