results = [
    ("Rob", 8),
    ("Aimee", 10),
    ("Gonzalo", 6),
    ("Graeme", 7)
]

for count, (name, answer) in enumerate(results, 1):
  print(f"{count}. {name} scored {answer}")

count = 1
for item in results:
  name = item[0]
  answer = item[1]
  print(f"{count}. {name} scored {answer}")
  count += 1

history = [
    (8, "message"),
    (5, "message"),
    (7, "message"),
    (10, "message"),
]

total = 0
lowest_value = 9999
highest_value = -9999

for answer, message in history:
    total = total + answer
    if lowest_value > answer:
        lowest_value = answer
    if highest_value < answer:
        highest_value = answer

print(f'The lowest value entered: {lowest_value}')
print(f'The highest value entered: {highest_value}')
print(f'Average value is: {total / len(history)}')
