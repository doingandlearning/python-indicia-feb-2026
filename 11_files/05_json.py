import csv

with open("movies.csv") as file:
  reader = csv.DictReader(file)
  # next(reader)  
  movies = []
  for row in reader:
    movies.append(row)

print([m for m in movies if m.get("Genre") == "Musical"])
print([m for m in movies if m.get("Year") == "1999"])