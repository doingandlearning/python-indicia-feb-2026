import csv

with open("movies.csv", mode="a") as file:
  writer = csv.DictWriter(file, fieldnames=["Title", "Year","Director", "Genre"])

  writer.writerow({
    "Title": "Speed",
    "Year":  1994,
    "Director": "Jan de Bont",
    "Genre": "Action"
  })