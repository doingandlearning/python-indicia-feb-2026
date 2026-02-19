from movieclass import Movie
import csv

with open("movies.csv") as file:
  reader = csv.DictReader(file)
  # next(reader)  
  movies = []
  for row in reader:
    movies.append(Movie(row["Title"], row["Year"], row["Director"], row["Genre"]))

print([m.to_dict() for m in movies if m.years_since_release() > 10])

with open("movies.csv", mode="a") as file:
  writer = csv.DictWriter(file, fieldnames=["Title", "Year", "Director", "Genre"])
  movie = Movie("Violent Night", 2022, "Tommy Wirkola", "Comedy")
  writer.writerow(movie.to_dict())