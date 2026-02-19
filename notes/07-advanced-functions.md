# 07: Advanced Functions - *args, Comprehensions, Lambda, and Functional Programming

## Why this matters

These tools make data-processing code shorter, more expressive, and more Pythonic. They're essential for working with collections efficiently.

Good advanced function usage gives you:
- Flexible function signatures
- Concise data transformations
- Functional programming patterns
- More readable code

---

## 1) Variable Arguments: `*args`

Accept an unknown number of arguments:

### Basic `*args`
```python
def add(*numbers):
    return sum(numbers)

# Can pass any number of arguments
print(add(1, 2))           # 3
print(add(1, 2, 3, 4, 5))  # 15
```

### How `*args` works
```python
def print_all(*args):
    for arg in args:
        print(arg)

print_all("apple", "banana", "cherry")
# Output:
# apple
# banana
# cherry
```

### `*args` collects into tuple
```python
def show_args(*args):
    print(type(args))  # <class 'tuple'>
    print(args)         # (1, 2, 3)

show_args(1, 2, 3)
```

### Combining with regular parameters
```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### Rule of thumb
- `*args` collects positional arguments into a tuple
- Use when argument count varies
- `*args` must come after regular parameters
- Name it `args` by convention (but can be any name)

---

## 2) Keyword Arguments: `**kwargs`

Accept an unknown number of keyword arguments:

### Basic `**kwargs`
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Edinburgh")
# Output:
# name: Alice
# age: 25
# city: Edinburgh
```

### How `**kwargs` works
```python
def show_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)        # {'name': 'Alice', 'age': 25}

show_kwargs(name="Alice", age=25)
```

### Combining `*args` and `**kwargs`
```python
def func(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

func("hello", 1, 2, 3, name="Alice", age=25)
# Output:
# Required: hello
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 25}
```

### Rule of thumb
- `**kwargs` collects keyword arguments into a dictionary
- Use when you need flexible keyword arguments
- `**kwargs` must come last
- Name it `kwargs` by convention

---

## 3) List Comprehensions

Create lists concisely in one line:

### Basic comprehension
```python
# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension (shorter)
squares = [x ** 2 for x in range(5)]
# Result: [0, 1, 4, 9, 16]
```

### Comprehension structure
```python
[expression for item in iterable]
```

### With condition (filtering)
```python
# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8]

# Traditional way
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
```

### Transforming data
```python
# Extract names from list of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
]

names = [person["name"] for person in people]
# Result: ["Alice", "Bob"]
```

### Nested comprehensions
```python
# Multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# Result: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### Rule of thumb
- Use comprehensions for simple transformations
- Keep comprehensions readable - split if too complex
- Comprehensions are faster than loops for simple operations
- Prefer comprehensions over `map()`/`filter()` for readability

---

## 4) Dictionary and Set Comprehensions

### Dictionary comprehension
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

### Set comprehension
```python
# Traditional way
squares = set()
for x in range(5):
    squares.add(x ** 2)

# Set comprehension
squares = {x ** 2 for x in range(5)}
# Result: {0, 1, 4, 9, 16}
```

---

## 5) Lambda Functions

Anonymous functions (functions without names):

### Basic lambda
```python
# Regular function
def double(x):
    return x * 2

# Lambda equivalent
double = lambda x: x * 2

print(double(5))  # 10
```

### Lambda syntax
```python
lambda parameters: expression
```

### Common use: Higher-order functions
```python
# With map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
# Result: [2, 4, 6, 8, 10]

# With filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4]

# With sorted()
people = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
sorted_by_age = sorted(people, key=lambda p: p["age"])
```

### Rule of thumb
- Use lambda for short, one-off functions
- Prefer named functions for complex logic
- Lambda is best with `map()`, `filter()`, `sorted()`
- Keep lambda expressions simple and readable

---

## 6) `map()`, `filter()`, and `reduce()`

### `map()` - Transform each element
```python
numbers = [1, 2, 3, 4, 5]

# Using map()
doubled = list(map(lambda x: x * 2, numbers))
# Result: [2, 4, 6, 8, 10]

# Equivalent list comprehension (preferred)
doubled = [x * 2 for x in numbers]
```

### `filter()` - Keep elements matching condition
```python
numbers = [1, 2, 3, 4, 5, 6]

# Using filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4, 6]

# Equivalent list comprehension (preferred)
evens = [x for x in numbers if x % 2 == 0]
```

### `reduce()` - Combine elements (requires import)
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce()
total = reduce(lambda x, y: x + y, numbers)
# Result: 15

# Equivalent built-in (preferred)
total = sum(numbers)
```

### Rule of thumb
- List comprehensions are usually more readable than `map()`/`filter()`
- Use `sum()` instead of `reduce()` for addition
- `map()`/`filter()` return iterators - convert to list if needed

---

## 7) Functional Programming Patterns

### Filtering data
```python
products = [
    {"name": "Laptop", "price": 999, "category": "Electronics"},
    {"name": "Book", "price": 15, "category": "Books"},
    {"name": "Phone", "price": 699, "category": "Electronics"},
]

# Filter electronics
electronics = [p for p in products if p["category"] == "Electronics"]

# Filter expensive items
expensive = [p for p in products if p["price"] > 500]
```

### Transforming data
```python
# Extract prices
prices = [p["price"] for p in products]

# Calculate totals with tax
with_tax = [p["price"] * 1.20 for p in products]  # 20% tax
```

### Combining operations
```python
# Expensive electronics
expensive_electronics = [
    p for p in products 
    if p["category"] == "Electronics" and p["price"] > 500
]
```

---

## Common Mistakes + Fixes

- **Mistake**: Very complex comprehensions  
  **Fix**: Split into multiple readable steps or use a loop

- **Mistake**: Overusing lambda for long logic  
  **Fix**: Use named `def` function for clarity

- **Mistake**: Magic tuple/list indexes (`p[2]`)  
  **Fix**: Document data shape clearly or use dictionaries

- **Mistake**: Forgetting `list()` with `map()`/`filter()`  
  **Fix**: They return iterators - convert: `list(map(...))`

- **Mistake**: Using `reduce()` when built-in exists  
  **Fix**: Use `sum()`, `max()`, `min()` instead of `reduce()`

- **Mistake**: Nested comprehensions that are hard to read  
  **Fix**: Use regular loops for complex nested logic

---

## Best Practices

1. **Prefer comprehensions over `map()`/`filter()`**
   ```python
   # Good - readable
   evens = [x for x in numbers if x % 2 == 0]
   
   # Avoid - less readable
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   ```

2. **Keep comprehensions simple**
   ```python
   # Good - clear intent
   squares = [x ** 2 for x in range(10)]
   
   # Avoid - too complex
   result = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10) if x > 5]
   ```

3. **Use lambda for simple, one-off functions**
   ```python
   # Good - simple lambda
   sorted_people = sorted(people, key=lambda p: p["age"])
   
   # Avoid - complex lambda (use named function)
   sorted_people = sorted(people, key=lambda p: p["address"]["city"].lower().strip())
   ```

4. **Document complex comprehensions**
   ```python
   # Good - comment explains logic
   # Filter products: electronics over $500
   expensive_electronics = [
       p for p in products 
       if p["category"] == "Electronics" and p["price"] > 500
   ]
   ```

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can accept variable arguments with `*args`
- [ ] I can accept keyword arguments with `**kwargs`
- [ ] I can rewrite simple loops as comprehensions
- [ ] I can filter collections by condition
- [ ] I can use lambda functions appropriately
- [ ] I understand when to use comprehensions vs loops
- [ ] I can combine filtering and transformation

---

## 60-Second Recap

- **`*args` handles flexible input** - Collects positional arguments into tuple
- **`**kwargs` handles keyword arguments** - Collects into dictionary
- **Comprehensions simplify transformations** - `[x**2 for x in range(10)]`
- **Lambda is for short functions** - Best with `map()`, `filter()`, `sorted()`
- **Prefer comprehensions** - More readable than `map()`/`filter()` in most cases
- **Keep it readable** - Split complex comprehensions into steps

---

## Mini Q&A

**Q: Is lambda faster than `def`?**  
A: Performance isn't the reason - brevity is. Use lambda for short, simple functions.

**Q: When should I avoid comprehensions?**  
A: When readability drops. Complex nested comprehensions are harder to read than loops.

**Q: What's the difference between `*args` and `**kwargs`?**  
A: `*args` collects positional arguments (tuple), `**kwargs` collects keyword arguments (dict).

**Q: Can I use both `*args` and `**kwargs`?**  
A: Yes - `*args` must come before `**kwargs`: `def func(required, *args, **kwargs):`

**Q: Should I use `map()` or list comprehension?**  
A: Prefer list comprehension - more readable: `[x*2 for x in nums]` vs `list(map(lambda x: x*2, nums))`

**Q: What does `reduce()` do?**  
A: Combines elements sequentially. Usually better alternatives exist (`sum()`, `max()`, etc.).

**Q: Can I use comprehensions with dictionaries?**  
A: Yes - dictionary comprehension: `{k: v for k, v in items}` and set comprehension: `{x for x in items}`.
