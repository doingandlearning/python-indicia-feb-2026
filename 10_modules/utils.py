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

print("Hello from the utils module!")