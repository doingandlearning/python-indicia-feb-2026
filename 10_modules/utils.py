"""
A utility file for doing useful things.
- use this in project blah, 
"""

def insecure_printer(message):
  print("I am an insecure printer")
  print(message)
  print("How did I do? Was it okay?")

class Shape:
  def __init__(self, type):
    self.type = type

triangle = Shape("triangle")

if __name__ == "__main__":
  print(f"Hello from the utils module! My name is {__name__}")
  # test code
  shape_type = input("What type of shape do you want to make? ")
  new_shape = Shape(shape_type)
  print(new_shape.type)