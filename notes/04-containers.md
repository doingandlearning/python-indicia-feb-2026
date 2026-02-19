# 04: Data Containers - Tuples, Lists, and Unpacking

## Why this matters

Containers let you group related values together. Instead of managing many separate variables, containers organize data efficiently.

Good container usage gives you:
- Organized data structures
- Efficient data processing
- Cleaner code
- Easier iteration and manipulation

---

## 1) Tuples (`tuple`)

Tuples are **ordered, indexable, and immutable** collections.

### Creating tuples
```python
# Parentheses (optional but recommended)
names = ("Alice", "Bob", "Charlie")

# Without parentheses (works but less clear)
names = "Alice", "Bob", "Charlie"

# Single element (note the comma!)
single = ("Alice",)  # Tuple
not_tuple = ("Alice")  # String!
```

### Tuple characteristics
- **Ordered** - Items have a defined order
- **Indexable** - Access items by position: `names[0]`
- **Immutable** - Cannot change after creation

### Accessing tuple elements
```python
names = ("Alice", "Bob", "Charlie")
print(names[0])   # "Alice"
print(names[1])   # "Bob"
print(names[-1])  # "Charlie" (last element)
```

### When to use tuples
- Fixed data that shouldn't change
- Returning multiple values from functions
- Dictionary keys (must be immutable)
- Grouping related values

### Rule of thumb
- Use tuples for fixed, read-only data
- Use tuples to return multiple values from functions
- Tuples signal "this structure should not change"

---

## 2) Lists (`list`)

Lists are **ordered, indexable, and mutable** collections.

### Creating lists
```python
# Square brackets
fruits = ["apple", "banana", "cherry"]

# Empty list
empty = []

# List with mixed types
mixed = [1, "hello", 3.14, True]
```

### List characteristics
- **Ordered** - Items have a defined order
- **Indexable** - Access items by position
- **Mutable** - Can add, remove, or modify items

### Common list operations

**Adding items:**
```python
fruits = ["apple", "banana"]
fruits.append("cherry")        # Add to end
fruits.insert(1, "orange")     # Insert at index 1
fruits.extend(["grape", "kiwi"])  # Add multiple items
```

**Removing items:**
```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")        # Remove by value
fruits.pop()                   # Remove last item
fruits.pop(0)                  # Remove item at index 0
del fruits[1]                  # Delete item at index 1
```

**Modifying items:**
```python
fruits = ["apple", "banana", "cherry"]
fruits[0] = "apricot"          # Change first item
```

**Finding items:**
```python
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")  # Find index (raises error if not found)
count = fruits.count("apple")   # Count occurrences
```

### When to use lists
- Data that needs to change
- Collections of similar items
- When you need to add/remove items
- Iterating over sequences

### Rule of thumb
- Use lists for collections that change
- Lists are the most common container type
- Lists are flexible and versatile

---

## 3) Indexing and Slicing

Both tuples and lists support indexing and slicing.

### Indexing (single element)
```python
items = ["apple", "banana", "cherry", "date"]

print(items[0])   # "apple" (first)
print(items[1])   # "banana"
print(items[-1])  # "date" (last)
print(items[-2])  # "cherry" (second to last)
```

### Slicing (multiple elements)
```python
items = ["apple", "banana", "cherry", "date", "elderberry"]

# Basic slice: [start:end] (end is exclusive)
print(items[1:3])    # ["banana", "cherry"]

# From start
print(items[:3])     # ["apple", "banana", "cherry"]

# To end
print(items[2:])     # ["cherry", "date", "elderberry"]

# All items
print(items[:])      # Full copy

# With step
print(items[::2])    # ["apple", "cherry", "elderberry"] (every 2nd)
print(items[::-1])   # Reversed
```

### Important slicing rules
- `[start:end]` - end is **exclusive** (not included)
- `[:end]` - from beginning to end (exclusive)
- `[start:]` - from start to end
- `[::-1]` - reverse the sequence

### Rule of thumb
- Remember: end index is exclusive
- Negative indices count from the end
- Slicing creates a new list/tuple (doesn't modify original)

---

## 4) Membership Testing

Use `in` and `not in` to check if an item exists:

```python
fruits = ["apple", "banana", "cherry"]

# Check membership
if "apple" in fruits:
    print("Found apple")

if "grape" not in fruits:
    print("No grape")
```

### Works with strings too
```python
text = "Hello World"
if "World" in text:
    print("Found!")
```

### Rule of thumb
- `in` - check if item exists
- `not in` - check if item doesn't exist
- Works with lists, tuples, strings, sets, dictionaries (keys)

---

## 5) Iteration Over Containers

### Basic iteration
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Iteration with index
```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

### Better: Using `enumerate()`
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### Iterating tuples
```python
names = ("Alice", "Bob", "Charlie")
for name in names:
    print(name)
```

---

## 6) Unpacking

Unpacking assigns multiple values at once:

### Basic unpacking
```python
# Tuple unpacking
point = (3, 4)
x, y = point
print(x)  # 3
print(y)  # 4

# List unpacking
colors = ["red", "green", "blue"]
r, g, b = colors
```

### Unpacking in loops
```python
# List of tuples
people = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Unpack in loop
for name, age in people:
    print(f"{name} is {age} years old")
```

### Unpacking with enumerate
```python
fruits = ["apple", "banana", "cherry"]
for count, fruit in enumerate(fruits, 1):  # Start at 1
    print(f"{count}. {fruit}")
```

### Unpacking function returns
```python
def get_name_age():
    return "Alice", 25

name, age = get_name_age()  # Unpack return value
```

### Extended unpacking
```python
# Get first and rest
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

# Get first, middle, last
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### Rule of thumb
- Unpacking improves readability vs manual indexing
- Use unpacking in loops when iterating over tuples/lists
- Unpacking makes code cleaner and more Pythonic

---

## 7) List Methods Summary

### Adding items
- `append(item)` - Add one item to end
- `insert(index, item)` - Insert at position
- `extend(iterable)` - Add multiple items

### Removing items
- `remove(item)` - Remove first occurrence (raises error if not found)
- `pop()` - Remove and return last item
- `pop(index)` - Remove and return item at index
- `clear()` - Remove all items

### Finding/searching
- `index(item)` - Find index (raises error if not found)
- `count(item)` - Count occurrences
- `in` / `not in` - Membership test

### Modifying
- `sort()` - Sort in place
- `reverse()` - Reverse in place
- `copy()` - Create shallow copy

### Information
- `len(list)` - Get length
- `max(list)` - Maximum value
- `min(list)` - Minimum value
- `sum(list)` - Sum (for numbers)

---

## 8) List Comprehensions (Preview)

List comprehensions create lists concisely:

```python
# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension (shorter)
squares = [x ** 2 for x in range(5)]
```

### With condition
```python
# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
```

**Note**: Comprehensions are covered more in Lab 07. This is just a preview.

---

## Common Mistakes + Fixes

- **Mistake**: Trying to update tuple values  
  **Fix**: Use a list if you need mutation: `items = ["apple", "banana"]`

- **Mistake**: Off-by-one slicing errors  
  **Fix**: Remember end index is exclusive: `items[0:3]` gives items 0, 1, 2

- **Mistake**: Hard-to-read index access  
  **Fix**: Prefer unpacking: `name, age = person` vs `name = person[0]`

- **Mistake**: Modifying list while iterating  
  **Fix**: Iterate over a copy: `for item in items.copy():`

- **Mistake**: Using `==` to compare lists  
  **Fix**: `==` works, but `is` checks identity (usually not what you want)

- **Mistake**: Forgetting that slicing creates a copy  
  **Fix**: Slicing doesn't modify original: `new_list = old_list[:]`

- **Mistake**: Single-element tuple without comma  
  **Fix**: `("item",)` not `("item")` (latter is a string)

---

## Best Practices

1. **Choose the right container**
   - Tuples for fixed data
   - Lists for mutable data
   - Don't use tuples just because they're "faster"

2. **Use meaningful variable names**
   ```python
   # Good
   student_names = ["Alice", "Bob"]
   
   # Avoid
   x = ["Alice", "Bob"]
   ```

3. **Prefer unpacking over indexing**
   ```python
   # Good
   name, age = person
   
   # Avoid (when possible)
   name = person[0]
   age = person[1]
   ```

4. **Use `enumerate()` when you need index**
   ```python
   # Good
   for i, item in enumerate(items):
       print(f"{i}: {item}")
   
   # Avoid
   for i in range(len(items)):
       print(f"{i}: {items[i]}")
   ```

5. **Be careful with list methods that modify**
   ```python
   # These modify the list in place
   items.sort()      # Sorts items
   items.reverse()   # Reverses items
   items.append(x)   # Adds x
   
   # These return new values
   sorted(items)     # Returns sorted copy
   reversed(items)   # Returns iterator
   ```

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can explain tuple vs list (immutable vs mutable)
- [ ] I can use indexing and slicing correctly
- [ ] I can loop through containers with `for`
- [ ] I can unpack tuple/list values cleanly
- [ ] I can use `in`/`not in` for membership testing
- [ ] I understand that slicing end index is exclusive
- [ ] I can use `enumerate()` when I need both index and value

---

## 60-Second Recap

- **Tuples are fixed records** - Immutable, use for data that shouldn't change
- **Lists are flexible sequences** - Mutable, use for collections that change
- **Indexing** - `items[0]` gets first, `items[-1]` gets last
- **Slicing** - `items[start:end]` (end exclusive), `items[:]` copies
- **Unpacking** - `name, age = person` is cleaner than indexing
- **Membership** - `in`/`not in` check existence
- **Iteration** - `for item in items:` loops through all items

---

## Mini Q&A

**Q: Why use tuples at all?**  
A: They signal "this structure should not change." Also used for dictionary keys and returning multiple values.

**Q: Best way to return multiple values from a function?**  
A: Return a tuple and unpack it: `return name, age` then `name, age = get_info()`

**Q: What's the difference between `append()` and `extend()`?**  
A: `append()` adds one item. `extend()` adds multiple items from an iterable.

**Q: How do I copy a list?**  
A: Use slicing: `new_list = old_list[:]` or `new_list = old_list.copy()`

**Q: Can I use negative indices?**  
A: Yes! `items[-1]` is the last item, `items[-2]` is second to last.

**Q: What happens if I slice beyond the list length?**  
A: Python handles it gracefully - returns what's available, no error.

**Q: How do I reverse a list?**  
A: `items.reverse()` modifies in place, or `reversed(items)` returns an iterator, or `items[::-1]` creates reversed copy.

**Q: Tuple with one element?**  
A: Need a comma: `("item",)` not `("item")` (latter is a string).
