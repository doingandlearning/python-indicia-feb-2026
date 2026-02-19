# 06: Functions - Reusable Logic

## Why this matters

Functions package logic into reusable units. Without functions, code repeats, is hard to test, and difficult to reason about.

Good function usage gives you:
- DRY code (Don't Repeat Yourself)
- Testable units
- Easier debugging
- Better organization
- Reusable logic

---

## 1) Defining and Calling Functions

### Basic function definition
```python
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Alice")  # Output: Hello, Alice!
```

### Function structure
```python
def function_name(parameters):
    """Optional docstring describing the function."""
    # Function body
    return value  # Optional return statement
```

### Rule of thumb
- `def` keyword starts function definition
- Function name follows variable naming rules
- Parameters in parentheses (can be empty)
- Colon `:` ends the definition line
- Body is indented

---

## 2) Parameters and Arguments

### Required parameters
```python
def add(a, b):
    return a + b

# Must provide both arguments
result = add(5, 3)  # 8
```

### Default parameters
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Use default
greet("Alice")              # Hello, Alice!

# Override default
greet("Bob", "Hi")          # Hi, Bob!
```

### Multiple defaults
```python
def print_message(message, divider_symbol="=", divider_length=20):
    print(divider_symbol * divider_length)
    print(message)
    print(divider_symbol * divider_length)

# Use all defaults
print_message("Hello")

# Override some defaults
print_message("Hello", "-", 30)

# Use keyword arguments
print_message("Hello", divider_length=30)
```

### Rule of thumb
- Required parameters must come first
- Default parameters come after required ones
- Use defaults for common values
- Keep defaults simple and predictable

---

## 3) Positional vs Keyword Arguments

### Positional arguments (by position)
```python
def subtract(a, b):
    return a - b

result = subtract(10, 3)  # 7 (a=10, b=3)
```

### Keyword arguments (by name)
```python
def subtract(a, b):
    return a - b

result = subtract(b=3, a=10)  # 7 (order doesn't matter)
```

### Mixing positional and keyword
```python
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b

# Positional first, then keyword
result = calculate(5, 3, operation="multiply")  # 15
```

### Rule of thumb
- Positional arguments must come before keyword arguments
- Keyword arguments improve readability
- Use keyword arguments for clarity with many parameters

---

## 4) Return Values

### Returning a single value
```python
def add(a, b):
    return a + b

result = add(5, 3)  # 8
```

### Returning multiple values (as tuple)
```python
def get_name_age():
    return "Alice", 25

# Unpack the return
name, age = get_name_age()
print(name)  # Alice
print(age)   # 25
```

### Returning None (implicit)
```python
def print_greeting(name):
    print(f"Hello, {name}!")
    # No return statement - returns None

result = print_greeting("Alice")  # None
```

### Early return
```python
def is_positive(number):
    if number <= 0:
        return False
    return True  # Only reached if number > 0
```

### Rule of thumb
- Use `return` when caller needs the result
- Functions without `return` return `None`
- Return early to simplify logic
- Return multiple values as a tuple (unpack on call)

---

## 5) Function Scope

Variables have scope - where they can be accessed:

### Local scope
```python
def my_function():
    local_var = "I'm local"
    print(local_var)

my_function()
# print(local_var)  # Error! Not accessible outside function
```

### Global scope
```python
global_var = "I'm global"

def my_function():
    print(global_var)  # Can read global

my_function()
print(global_var)  # Also accessible here
```

### Modifying global variables
```python
count = 0

def increment():
    global count  # Must declare global to modify
    count += 1

increment()
print(count)  # 1
```

### Rule of thumb
- Variables inside functions are local
- Can read global variables without `global`
- Must use `global` keyword to modify globals
- Prefer passing parameters over globals

---

## 6) Built-in Functions

Python provides many built-in functions. Know these common ones:

### Type conversion
```python
int("42")        # 42
float("3.14")    # 3.14
str(42)          # "42"
bool(1)          # True
```

### Math operations
```python
abs(-5)          # 5
max(1, 2, 3)     # 3
min(1, 2, 3)     # 1
sum([1, 2, 3])   # 6
round(3.14159, 2)  # 3.14
```

### Sequence operations
```python
len([1, 2, 3])   # 3
sorted([3, 1, 2]) # [1, 2, 3]
reversed([1, 2, 3])  # Iterator
enumerate(["a", "b"])  # Iterator of (index, value)
```

### Input/output
```python
print("Hello")           # Output
input("Enter name: ")    # Input (returns string)
```

### Type checking
```python
type(42)         # <class 'int'>
isinstance(42, int)  # True
```

### Rule of thumb
- Check built-ins before writing custom functions
- `len()`, `sum()`, `max()`, `min()` are very common
- `sorted()` returns new list, doesn't modify original

---

## 7) Docstrings

Document your functions:

```python
def calculate_total(price, quantity, discount=0):
    """
    Calculate total price with optional discount.
    
    Args:
        price: Unit price (float)
        quantity: Number of items (int)
        discount: Discount percentage (float, default 0)
    
    Returns:
        Total price as float
    """
    total = price * quantity
    if discount > 0:
        total *= (1 - discount / 100)
    return total
```

### Accessing docstrings
```python
print(calculate_total.__doc__)
help(calculate_total)
```

### Rule of thumb
- Add docstrings to all functions
- Describe what function does, parameters, and return value
- Use triple quotes for multi-line docstrings

---

## 8) Function Best Practices

### Keep functions focused
```python
# Good - single responsibility
def calculate_subtotal(items):
    return sum(item['price'] for item in items)

def apply_discount(subtotal, discount_percent):
    return subtotal * (1 - discount_percent / 100)

# Avoid - does too much
def process_order(items, discount):
    # Calculates subtotal, applies discount, prints receipt...
    pass
```

### Use meaningful names
```python
# Good
def calculate_total_price(items):
    ...

# Avoid
def calc(items):
    ...
```

### Keep functions small
```python
# Good - easy to understand
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

# Avoid - too complex, split into smaller functions
def validate_user(email, password, age, ...):
    # 50 lines of validation logic
    pass
```

### Prefer parameters over globals
```python
# Good
def calculate_total(price, quantity):
    return price * quantity

# Avoid
price = 10
quantity = 5
def calculate_total():
    return price * quantity  # Uses globals
```

---

## Common Mistakes + Fixes

- **Mistake**: Printing instead of returning  
  **Fix**: Use `return` when caller needs the value

- **Mistake**: Wrong argument order  
  **Fix**: Match function signature or use keyword arguments

- **Mistake**: Overly large functions  
  **Fix**: Split by responsibility into smaller functions

- **Mistake**: Modifying global variables without `global`  
  **Fix**: Use `global` keyword or pass as parameter

- **Mistake**: Forgetting return statement  
  **Fix**: Functions without `return` return `None`

- **Mistake**: Default parameter with mutable value  
  **Fix**: Use `None` and create inside function:
  ```python
  # Bad
  def add_item(item, items=[]):  # Mutable default!
      items.append(item)
      return items
  
  # Good
  def add_item(item, items=None):
      if items is None:
          items = []
      items.append(item)
      return items
  ```

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can define functions with `def`
- [ ] I can use parameters and defaults correctly
- [ ] I can return values and compose function calls
- [ ] I can write small, focused functions
- [ ] I understand function scope (local vs global)
- [ ] I use docstrings to document functions
- [ ] I prefer parameters over global variables

---

## 60-Second Recap

- **Functions package logic** - Reusable units of code
- **Parameters are inputs** - Pass data into functions
- **Return values are outputs** - Functions can return results
- **Scope matters** - Local vs global variables
- **Keep functions focused** - One responsibility per function
- **Use docstrings** - Document what functions do

---

## Mini Q&A

**Q: Should every function return something?**  
A: Not always. Return when caller needs the result. Functions without `return` return `None`.

**Q: When are defaults useful?**  
A: When a common value applies most of the time. Makes functions more flexible.

**Q: Can I have a function with no parameters?**  
A: Yes: `def greet(): print("Hello")` - empty parentheses.

**Q: What's the difference between parameters and arguments?**  
A: Parameters are in function definition (`def func(param):`). Arguments are values passed when calling (`func(arg)`).

**Q: Can I return multiple values?**  
A: Yes - return a tuple: `return a, b` then unpack: `x, y = func()`.

**Q: How do I modify a global variable?**  
A: Use `global` keyword: `global var_name` then modify it.

**Q: What happens if I don't return anything?**  
A: Function returns `None` implicitly.

**Q: Can I use a function before it's defined?**  
A: No - functions must be defined before they're called (unless inside another function that's called later).
