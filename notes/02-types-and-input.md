# 02: Variables, Types, Strings, and Input

## Why this matters

Understanding types prevents most beginner bugs. Type mismatches cause runtime errors, and input handling is where real programs interact with users.

Good type handling gives you:
- Fewer runtime errors
- Clearer code intent
- Better user experience
- Easier debugging

---

## 1) Core Python Types

Python has several built-in types. Know these four essentials:

### Integer (`int`)
Whole numbers (positive, negative, or zero).

```python
age = 42
count = -5
zero = 0
print(type(age))  # <class 'int'>
```

### Float (`float`)
Decimal numbers.

```python
price = 19.99
temperature = -5.5
pi = 3.14159
print(type(price))  # <class 'float'>
```

### String (`str`)
Text data (always in quotes).

```python
name = "Alice"
greeting = 'Hello'
message = """Multi-line
string"""
print(type(name))  # <class 'str'>
```

### Boolean (`bool`)
Logical values: `True` or `False`.

```python
is_active = True
is_complete = False
print(type(is_active))  # <class 'bool'>
```

### Rule of thumb
- Numbers without decimals → `int`
- Numbers with decimals → `float`
- Text in quotes → `str`
- `True`/`False` → `bool`

---

## 2) Type Checking

Use `type()` to inspect what type a variable is:

```python
value = 42
print(type(value))  # <class 'int'>

value = "42"
print(type(value))  # <class 'str'>
```

**Common use**: Debugging type errors by checking what you actually have.

---

## 3) Type Conversion

Convert between types using constructor functions:

### Converting to Integer
```python
age_str = "25"
age = int(age_str)
print(age + 1)  # 26

# Works with floats (truncates)
price = int(19.99)  # 19
```

### Converting to Float
```python
price_str = "19.99"
price = float(price_str)
print(price * 2)  # 39.98

# Works with integers
count = float(5)  # 5.0
```

### Converting to String
```python
age = 25
age_str = str(age)
print("Age: " + age_str)  # "Age: 25"

# Useful for concatenation
result = "The answer is " + str(42)
```

### Converting to Boolean
```python
# Truthy values become True
bool(1)      # True
bool("text") # True
bool([1,2])  # True

# Falsy values become False
bool(0)      # False
bool("")     # False
bool([])     # False
bool(None)   # False
```

### Rule of thumb
- `int()` - for whole numbers
- `float()` - for decimals
- `str()` - for text representation
- `bool()` - for truthiness checks

---

## 4) String Formatting with f-strings

f-strings (formatted string literals) are the modern way to embed variables in strings.

### Basic f-string
```python
name = "Alice"
age = 25
message = f"My name is {name} and I'm {age} years old"
print(message)
# Output: My name is Alice and I'm 25 years old
```

### Expressions in f-strings
```python
price = 19.99
quantity = 3
total = f"Total: ${price * quantity:.2f}"
print(total)
# Output: Total: $59.97
```

### Formatting numbers
```python
pi = 3.14159
print(f"Pi rounded: {pi:.2f}")  # Pi rounded: 3.14
print(f"Pi percentage: {pi:.1%}")  # Pi percentage: 314.2%
```

### Rule of thumb
- Use f-strings for all string formatting
- Prefer f-strings over `.format()` or `%` formatting
- Use `:.2f` for 2 decimal places in numbers

---

## 5) User Input with `input()`

`input()` reads text from the user and **always returns a string**.

### Basic input
```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

### Converting input
```python
# Input always returns string - convert for numbers!
age_str = input("What is your age? ")
age = int(age_str)  # Convert to integer
print(f"Next year you'll be {age + 1}")
```

### Handling input errors
```python
try:
    age_str = input("What is your age? ")
    age = int(age_str)
    print(f"Next year you'll be {age + 1}")
except ValueError:
    print("Please enter a valid number")
```

### Cleaning input
```python
# Remove whitespace
name = input("Name: ").strip()

# Convert to lowercase
email = input("Email: ").lower().strip()
```

### Rule of thumb
- `input()` always returns `str`
- Always convert numeric input: `int(input(...))` or `float(input(...))`
- Use `.strip()` to remove leading/trailing whitespace
- Handle conversion errors with `try/except`

---

## 6) Common Type Operations

### String operations
```python
text = "Hello World"
print(text.upper())      # "HELLO WORLD"
print(text.lower())      # "hello world"
print(text.strip())      # Remove whitespace
print(len(text))         # 11
print(text.replace("World", "Python"))  # "Hello Python"
```

### Number operations
```python
# Arithmetic
result = 10 + 5    # 15
result = 10 - 5    # 5
result = 10 * 5    # 50
result = 10 / 5    # 2.0 (always float)
result = 10 // 5   # 2 (integer division)
result = 10 % 3    # 1 (modulo/remainder)
result = 10 ** 2   # 100 (exponentiation)

# Comparison
print(5 > 3)   # True
print(5 == 3)  # False
print(5 != 3)  # True
```

---

## 7) Type Coercion and Mixing Types

### What happens when you mix types?

**String + Number = Error**
```python
age = 25
# This fails:
message = "Age: " + age  # TypeError!
# Fix:
message = "Age: " + str(age)
```

**Number + String = Error**
```python
age = "25"
# This fails:
result = age + 1  # TypeError!
# Fix:
result = int(age) + 1
```

**Float + Integer = Float**
```python
result = 5.5 + 2  # 7.5 (float)
```

### Rule of thumb
- Explicit conversion is safer than implicit
- Convert early, not late
- Use `str()` when concatenating strings
- Use `int()`/`float()` when doing math

---

## Common Mistakes + Fixes

- **Mistake**: Adding string and number without conversion  
  **Fix**: Convert first: `str(number)` or `int(string)`

- **Mistake**: Assuming `input()` returns a number  
  **Fix**: Always convert: `int(input(...))` or `float(input(...))`

- **Mistake**: Unexpected spaces in input  
  **Fix**: Use `.strip()`: `input("Name: ").strip()`

- **Mistake**: Comparing string numbers: `"5" > "10"` (lexicographic)  
  **Fix**: Convert to numbers: `int("5") > int("10")`

- **Mistake**: Using `==` to compare floats (precision issues)  
  **Fix**: Check if close: `abs(a - b) < 0.0001` or use integers

- **Mistake**: Forgetting that division always returns float  
  **Fix**: Use `//` for integer division if needed

---

## Best Practices

1. **Convert input immediately** - Don't store string numbers
   ```python
   # Good
   age = int(input("Age: "))
   
   # Avoid
   age_str = input("Age: ")
   # ... later ...
   age = int(age_str)
   ```

2. **Use f-strings consistently** - They're readable and modern
   ```python
   # Good
   print(f"Name: {name}, Age: {age}")
   
   # Avoid
   print("Name: " + name + ", Age: " + str(age))
   ```

3. **Check types when debugging** - Use `type()` to verify
   ```python
   print(f"Type: {type(value)}")  # Debug helper
   ```

4. **Handle conversion errors** - Wrap risky conversions in try/except
   ```python
   try:
       age = int(input("Age: "))
   except ValueError:
       print("Invalid number")
   ```

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can identify each core type (`int`, `float`, `str`, `bool`)
- [ ] I can use f-strings confidently for output
- [ ] I can convert user input before calculations
- [ ] I can debug with `type()` when needed
- [ ] I handle input errors gracefully
- [ ] I use `.strip()` to clean user input

---

## 60-Second Recap

- **Types control what operations are valid** - You can't add a string to a number
- **Strings are not numbers until converted** - `input()` always returns strings
- **f-strings are the modern way** - Use `f"Text {variable}"` for formatting
- **Convert early, not late** - Convert input immediately after receiving it
- **Type errors are common** - Use `type()` to debug, convert explicitly

---

## Mini Q&A

**Q: Why does `"5" + 1` fail?**  
A: It mixes `str` and `int`. Python doesn't auto-convert. Use `int("5") + 1` or `"5" + str(1)`.

**Q: Best way to print variables in text?**  
A: f-strings: `f"Name: {name}, Age: {age}"`. They're readable and handle types automatically.

**Q: Why does `input()` return a string?**  
A: Users type text. Python doesn't know if "42" should be a number or text. You decide with conversion.

**Q: When should I use `int()` vs `float()`?**  
A: Use `int()` for whole numbers (counts, ages). Use `float()` for decimals (prices, measurements).

**Q: What's the difference between `5 / 2` and `5 // 2`?**  
A: `/` returns float (2.5), `//` returns integer (2). Use `//` when you need whole number division.

**Q: How do I check if a string can be converted to a number?**  
A: Use try/except:
```python
try:
    number = int(user_input)
except ValueError:
    print("Not a valid number")
```

**Q: What's `None`?**  
A: `None` represents "no value" or "empty". It's its own type. Use it when a variable might not have a value yet.
