empty_list = []
print(empty_list)
print(type(empty_list))

beatles_list = ["John", "Paul", "George", "Ringo"]
print(beatles_list[0])

if "Kevin" in beatles_list:
  print("It's a miracle!")
else:
  print("That was expected.")

for beatle in beatles_list:
  print(beatle)

beatles_list.append("Graeme")
print(beatles_list)

beatles_list.extend(("Rob", "Gonzalo", "John"))
print(beatles_list)

beatles_list.insert(2, "Aimee")
print(beatles_list)

print(beatles_list.count("John"))

while "John" in beatles_list:
  beatles_list.remove("John")

print(beatles_list)

last_member = beatles_list.pop()
print(beatles_list)
print(f"We removed {last_member } from our list.")

# while len(beatles_list) > 0:
#   print(beatles_list.pop())

del beatles_list[-1]
print(beatles_list)

beatles_list[0] = "Kevin"
print(beatles_list)

beatles_list.reverse()
print(beatles_list)

beatles_list.sort()
print(beatles_list)

print(list(tuple(beatles_list)))