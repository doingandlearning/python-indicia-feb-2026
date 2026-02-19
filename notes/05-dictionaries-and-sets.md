# 05: Advanced Data Containers - Dictionaries, Sets, and Comprehensions

## Why this matters

Real applications work with labeled data (dictionaries) and need to handle uniqueness and set operations (sets). These containers solve problems that lists and tuples can't handle efficiently.

Good advanced container usage gives you:
- Fast lookups by key (dictionaries)
- Efficient uniqueness handling (sets)
- Clean data modeling
- Powerful set operations

---

## 1) Dictionaries (`dict`)

Dictionaries store **key-value pairs** for fast lookups by key.

### Creating dictionaries
```python
# Curly braces with key:value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "Edinburgh"
}

# Empty dictionary
empty = {}

# Using dict() constructor
person = dict(name="Alice", age=25, city="Edinburgh")
```

### Dictionary characteristics
- **Unordered** (Python 3.7+ maintains insertion order)
- **Mutable** - Can add, remove, modify items
- **Keys must be immutable** (strings, numbers, tuples)
- **Values can be anything**

### Accessing dictionary values
```python
person = {"name": "Alice", "age": 25}

# Using bracket notation
print(person["name"])  # "Alice"

# Using .get() (safer - returns None if key missing)
print(person.get("name"))        # "Alice"
print(person.get("email"))       # None
print(person.get("email", "N/A"))  # "N/A" (default value)
```

### Modifying dictionaries
```python
person = {"name": "Alice"}

# Add or update
person["age"] = 25           # Add new key
person["name"] = "Bob"       # Update existing key

# Remove items
del person["age"]            # Delete key
email = person.pop("email", None)  # Remove and return (with default)
person.clear()               # Remove all items
```

### Dictionary methods

**Getting keys, values, items:**
```python
person = {"name": "Alice", "age": 25}

# Get all keys
keys = person.keys()         # dict_keys(['name', 'age'])

# Get all values
values = person.values()     # dict_values(['Alice', 25])

# Get key-value pairs
items = person.items()       # dict_items([('name', 'Alice'), ('age', 25)])

# Iterate over items
for key, value in person.items():
    print(f"{key}: {value}")
```

**Checking membership:**
```python
person = {"name": "Alice", "age": 25}

# Check if key exists
if "name" in person:
    print("Name exists")

# Check if key doesn't exist
if "email" not in person:
    print("No email")
```

### When to use dictionaries
- Storing labeled data (like a database record)
- Fast lookups by key
- Mapping relationships
- Configuration data
- Counting occurrences

### Rule of thumb
- Use dictionaries for labeled, structured data
- Use `.get()` when key might not exist
- Use `in` to check key existence
- Dictionaries are Python's most versatile data structure

---

## 2) Nested Data Structures

Real-world data is often nested (dictionaries containing lists, lists containing dictionaries, etc.):

```python
# List of dictionaries (common pattern)
students = [
    {"name": "Alice", "age": 25, "grades": [85, 90, 88]},
    {"name": "Bob", "age": 23, "grades": [92, 87, 91]},
]

# Accessing nested data
print(students[0]["name"])           # "Alice"
print(students[0]["grades"][0])     # 85

# Dictionary containing lists
person = {
    "name": "Alice",
    "hobbies": ["reading", "coding", "hiking"],
    "address": {
        "street": "123 Main St",
        "city": "Edinburgh",
        "postcode": "EH1 1AB"
    }
}

# Accessing nested dictionary
print(person["address"]["city"])    # "Edinburgh"
```

### Navigating nested structures
```python
# Check if nested key exists
if "address" in person and "city" in person["address"]:
    print(person["address"]["city"])

# Safer with .get()
city = person.get("address", {}).get("city", "Unknown")
```

### Rule of thumb
- Inspect structure first, then access level by level
- Use `.get()` with defaults for safe navigation
- Nested data is normal in real APIs and data files

---

## 3) Sets (`set`)

Sets store **unique, unordered** values. Great for deduplication and set operations.

### Creating sets
```python
# Curly braces (but not key:value!)
fruits = {"apple", "banana", "cherry"}

# Empty set (must use set(), not {})
empty = set()

# From a list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
```

### Set characteristics
- **Unordered** - No guaranteed order
- **Unique** - No duplicates allowed
- **Mutable** - Can add/remove items
- **Fast membership testing**

### Set operations

**Adding and removing:**
```python
fruits = {"apple", "banana"}
fruits.add("cherry")        # Add one item
fruits.remove("apple")      # Remove (raises error if missing)
fruits.discard("grape")     # Remove (no error if missing)
fruits.pop()                # Remove and return arbitrary item
fruits.clear()              # Remove all items
```

**Set math operations:**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Intersection (items in both)
print(set1 & set2)                    # {3, 4}
print(set1.intersection(set2))        # {3, 4}

# Union (items in either)
print(set1 | set2)                    # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))               # {1, 2, 3, 4, 5, 6}

# Difference (items in set1 but not set2)
print(set1 - set2)                    # {1, 2}
print(set1.difference(set2))          # {1, 2}

# Symmetric difference (items in either, but not both)
print(set1 ^ set2)                    # {1, 2, 5, 6}
print(set1.symmetric_difference(set2)) # {1, 2, 5, 6}
```

**Membership testing:**
```python
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)      # True
print("grape" not in fruits)  # True
```

### When to use sets
- Removing duplicates from a list
- Fast membership testing
- Set operations (intersection, union, etc.)
- Tracking unique items

### Common pattern: Deduplication
```python
# Remove duplicates from list
countries = ["Scotland", "Scotland", "England", "Netherlands"]
unique_countries = list(set(countries))
# Result: ["Scotland", "England", "Netherlands"] (order may vary)
```

### Rule of thumb
- Use sets for uniqueness and set operations
- Sets are unordered - don't rely on order
- Sets are fast for membership testing (`in`)

---

## 4) Frozen Sets (`frozenset`)

Immutable version of sets (like tuple is to list):

```python
# Create frozenset
frozen = frozenset([1, 2, 3])

# Can use as dictionary key (sets can't)
key = frozenset([1, 2, 3])
data = {key: "value"}
```

**Use case**: When you need an immutable set (rare, but useful for dictionary keys).

---

## 5) Dictionary Comprehensions

Create dictionaries concisely:

```python
# Traditional way
squares = {}
for x in range(5):
    squares[x] = x ** 2

# Dictionary comprehension
squares = {x: x ** 2 for x in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
```

### Transforming data
```python
# Convert list of tuples to dictionary
pairs = [("name", "Alice"), ("age", 25), ("city", "Edinburgh")]
person = {key: value for key, value in pairs}
# Result: {"name": "Alice", "age": 25, "city": "Edinburgh"}
```

---

## 6) Set Comprehensions

Create sets concisely:

```python
# Traditional way
squares = set()
for x in range(5):
    squares.add(x ** 2)

# Set comprehension
squares = {x ** 2 for x in range(5)}
# Result: {0, 1, 4, 9, 16}

# With condition
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}
```

---

## 7) Common Patterns

### Counting occurrences
```python
# Count items in a list
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
# Result: {"apple": 3, "banana": 2, "cherry": 1}

# Using collections.Counter (advanced)
from collections import Counter
counts = Counter(items)
```

### Grouping data
```python
# Group students by grade
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
]

grouped = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped:
        grouped[grade] = []
    grouped[grade].append(student["name"])
# Result: {"A": ["Alice", "Charlie"], "B": ["Bob"]}
```

### Finding common elements
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find common items
common = set(list1) & set(list2)  # {4, 5}
```

---

## Common Mistakes + Fixes

- **Mistake**: `dict[key]` on missing key raises KeyError  
  **Fix**: Use `.get(key, default)` when key might not exist

- **Mistake**: Expecting stable order in sets  
  **Fix**: Treat sets as unordered (though Python 3.7+ maintains insertion order)

- **Mistake**: Losing duplicates unintentionally  
  **Fix**: Only convert to set when uniqueness is required

- **Mistake**: Using mutable types as dictionary keys  
  **Fix**: Keys must be immutable (strings, numbers, tuples, frozensets)

- **Mistake**: Confusing `{}` for empty set  
  **Fix**: `{}` is an empty dict, use `set()` for empty set

- **Mistake**: Modifying dictionary while iterating  
  **Fix**: Iterate over `.keys()`, `.values()`, or `.items()` copy

- **Mistake**: Using `==` to compare sets (order doesn't matter)  
  **Fix**: `==` works correctly for sets (order-independent)

---

## Best Practices

1. **Use `.get()` for safe access**
   ```python
   # Good
   email = person.get("email", "N/A")
   
   # Avoid (raises KeyError if missing)
   email = person["email"]
   ```

2. **Use dictionary for labeled data**
   ```python
   # Good - clear labels
   person = {"name": "Alice", "age": 25}
   
   # Avoid - unclear what indices mean
   person = ["Alice", 25]
   ```

3. **Use sets for uniqueness**
   ```python
   # Good - removes duplicates
   unique_items = list(set(items))
   
   # Avoid - manual checking
   unique_items = []
   for item in items:
       if item not in unique_items:
           unique_items.append(item)
   ```

4. **Use comprehensions for transformations**
   ```python
   # Good - concise
   squares = {x: x**2 for x in range(10)}
   
   # Avoid - verbose
   squares = {}
   for x in range(10):
       squares[x] = x ** 2
   ```

5. **Navigate nested structures safely**
   ```python
   # Good - safe navigation
   city = person.get("address", {}).get("city", "Unknown")
   
   # Avoid - raises KeyError if missing
   city = person["address"]["city"]
   ```

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can model data with dictionaries (key-value pairs)
- [ ] I can use `.get()` for safe dictionary access
- [ ] I can navigate nested data structures safely
- [ ] I can use set operations (intersection, union, difference)
- [ ] I can dedupe a list using sets
- [ ] I understand that sets are unordered
- [ ] I can use dictionary and set comprehensions
- [ ] I can iterate over dictionary items with `.items()`

---

## 60-Second Recap

- **Dictionaries map labels to values** - Fast lookups by key
- **Use `.get()` for safe access** - Returns default if key missing
- **Nested data is normal** - Dictionaries containing lists/dicts
- **Sets store unique values** - Great for deduplication
- **Set operations** - `&` (intersection), `|` (union), `-` (difference)
- **Comprehensions** - Create dicts/sets concisely
- **Membership testing** - `in`/`not in` works with dicts (keys) and sets

---

## Mini Q&A

**Q: Dict or list for user records?**  
A: Dict for each record's fields (labeled data), list for many records: `[{"name": "Alice"}, {"name": "Bob"}]`

**Q: Why did item order change after converting to set?**  
A: Sets are unordered by design. Order is not guaranteed (though Python 3.7+ maintains insertion order).

**Q: What's the difference between `.get()` and bracket notation?**  
A: `.get()` returns `None` (or default) if key missing. Bracket notation raises `KeyError`.

**Q: Can I use a list as a dictionary key?**  
A: No - keys must be immutable. Use a tuple instead: `{(1, 2): "value"}`

**Q: How do I remove duplicates from a list?**  
A: `unique = list(set(original))` - converts to set (removes duplicates), then back to list.

**Q: What's the difference between `remove()` and `discard()` for sets?**  
A: `remove()` raises error if item missing. `discard()` does nothing if missing.

**Q: Can dictionaries have duplicate keys?**  
A: No - later value overwrites earlier one. Keys must be unique.

**Q: How do I merge two dictionaries?**  
A: `dict1.update(dict2)` modifies dict1, or `{**dict1, **dict2}` creates new dict (Python 3.5+).
