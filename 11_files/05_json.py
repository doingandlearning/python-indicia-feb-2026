import csv
import json

with open("movies.csv") as file:
  reader = csv.DictReader(file)
  movies = []
  for row in reader:
    movies.append(row)

with open("movies.json", mode="w") as file:
  file.write(json.dumps(movies, indent=2))