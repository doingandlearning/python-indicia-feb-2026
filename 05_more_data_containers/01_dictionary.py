# key (label) -> value (actual data) pairs
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

cities = {
  "Scotland": "Edinburgh",
  "England": "London",
  "Netherlands": "Amsterdam",
  "Italy": "Rome"
}

print(cities["Scotland"])
print(cities.get("Scotland", "Unknown country")) # safer way to access data in the dictionary

cities["Scotland"] = "Glasgow"
print(cities)

cities.update({"Netherlands": "The Hague", "England": "Brighton", "Northern Ireland": "Belfast"})
print(cities)

print(len(cities))
print("Brighton" in cities)

print(list(cities.keys()))
print(list(cities.values()))
print(list(cities.items()))

for country, capital in cities.items():
  print(f"{capital} is the capital of {country}")