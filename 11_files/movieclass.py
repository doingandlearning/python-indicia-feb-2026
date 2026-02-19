from datetime import date

class Movie:
  def __init__(self, title, year, director, genre):
    self.title = title
    self.year = year
    self.director = director
    self.genre = genre

  def __str__(self):
    return f"{self.title}[{self.genre}] released {self.year}, directed by {self.director}"
  
  def to_dict(self):
    return {
      "Title": self.title,
      "Year": self.year,
      "Genre": self.genre,
      "Director": self.director
    }
  
  def years_since_release(self):
    return date.today().year - int(self.year) 