def add(*numbers):  
  print("1st one")
  total = 0
  for number in numbers:
    total += number
  return total

print(add(1,2))

def add(*numbers):
  print("Second one")
  return sum(numbers)


print(add(1,2))
####

numbers = [1,4,9,16,25,36,49]
first, second, *rest = numbers

print(first)
print(second)
print(rest)


# 
# print(add(1,2))
# print(add(4,5))
# print(add(2,3))
# print(add(1,2,3))
# print(add(3,4,5))
# print(add(1,2,3,4))
# print(add(3,4,5,5))
# print(add(4))

def input(prompt):
  print("I don't care what you think")
  return 42

favourite_number = input("What is your favourite number?")
print(favourite_number)


# List comprehension -> map, filter
# lambda