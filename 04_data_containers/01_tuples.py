# tuples 

empty_tuple = ()  # for single valued tuples, put a comma after the value.
print(empty_tuple)
print(type(empty_tuple))

#               0       1        2          3     <- index or position
name_tuple = ("Rob", "Aimee", "Gonzalo", "Graeme")

print(name_tuple[2])
print(name_tuple[1:])
print(name_tuple[:2])
print(name_tuple[1:3])

print("Kevin" in name_tuple)  # check for membership
print("Rob" in name_tuple)

if "Kevin" not in name_tuple:
  print("Unauthorized.")
else:
  print("Here's the data.")

for person in name_tuple:
  print(f"{person} is enjoying a Python course.")

print(name_tuple.count("Kevin"))

name_to_look_for = "Gonzalo"

if name_to_look_for in name_tuple:
  print(f"{name_to_look_for} is at index {name_tuple.index(name_to_look_for)}")
else:
  print(f"{name_to_look_for} is not in tuple.")

countries = ("Scotland", "Northern Ireland", "Netherlands")

all_of_us = (name_tuple, countries)
print(all_of_us)

print(all_of_us[1][1])  # Northern Ireland

print(("String", 1, True, (0.1, 0.1) ))