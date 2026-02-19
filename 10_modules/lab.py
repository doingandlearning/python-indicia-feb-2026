def filter_data(data, condition_func):
    """Filter data based on a condition function."""
    return [item for item in data if condition_func(item)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["apple", "banana", "kiwi", "grape", "pear", "strawberry"]
people = [
  {"name": "Alice", "age": 30},
  {"name": "Bob", "age": 17},
  {"name": "Charlie", "age": 25},
  {"name": "Diana", "age": 15},
]

print(filter_data(numbers, lambda x: x < 5))
print(filter_data(words, lambda x: len(x) > 5))


# Example conditions
is_even = lambda n: n % 2 == 0
long_word = lambda w: len(w) > 5
is_adult = lambda person: person["age"] >= 18