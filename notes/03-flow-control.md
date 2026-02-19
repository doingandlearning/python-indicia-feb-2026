# 03: Flow Control - Decisions, Loops, and Control Flow

## Why this matters

Flow control decides what your program does next. Without it, programs run line-by-line with no decisions or repetition. Real programs need conditionals and loops.

Good flow control gives you:
- Programs that make decisions
- Code that repeats efficiently
- Interactive user experiences
- Logic that handles different scenarios

---

## 1) Conditional Statements: `if`, `elif`, `else`

Conditionals let your program choose different paths based on conditions.

### Basic `if` statement
```python
age = 18
if age >= 18:
    print("You are an adult")
```

### `if` with `else`
```python
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### Multiple conditions with `elif`
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")
```

### Rule of thumb
- `if` - first condition to check
- `elif` - additional conditions (can have many)
- `else` - catch-all (optional, only one)

---

## 2) Comparison Operators

Use these to create conditions:

```python
# Equality
x == y   # Equal to
x != y   # Not equal to

# Comparison
x < y    # Less than
x > y    # Greater than
x <= y   # Less than or equal
x >= y   # Greater than or equal

# Examples
age = 25
if age >= 18:
    print("Adult")

if age != 0:
    print("Not zero")
```

### String comparisons
```python
name = "Alice"
if name == "Alice":
    print("Hello Alice")

# Lexicographic (alphabetical) comparison
if "apple" < "banana":  # True
    print("apple comes first")
```

---

## 3) Logical Operators

Combine multiple conditions:

### `and` - Both must be true
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
```

### `or` - At least one must be true
```python
age = 16
has_parent = True

if age >= 18 or has_parent:
    print("Can enter")
```

### `not` - Invert the condition
```python
is_weekend = False

if not is_weekend:
    print("It's a weekday")
```

### Combining operators
```python
age = 25
has_license = True
has_car = False

if (age >= 18 and has_license) or has_car:
    print("Can drive")
```

### Rule of thumb
- Use `and` when both conditions must be true
- Use `or` when at least one must be true
- Use `not` to invert a boolean
- Use parentheses to clarify complex logic

---

## 4) Nested Conditionals

You can nest `if` statements inside other `if` statements:

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need a license")
else:
    print("Too young")
```

### Flattening nested conditions
```python
# Nested (harder to read)
if age >= 18:
    if has_license:
        print("Can drive")

# Flattened (better)
if age >= 18 and has_license:
    print("Can drive")
```

### Rule of thumb
- Avoid deep nesting (more than 2-3 levels)
- Flatten with `and`/`or` when possible
- Use `elif` instead of nested `if` when checking related conditions

---

## 5) Ternary Expressions (Conditional Expressions)

Short way to assign based on a condition:

```python
# Traditional way
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary way (shorter)
status = "adult" if age >= 18 else "minor"
```

### When to use
- Simple assignments based on one condition
- Keep it readable - don't nest ternaries

---

## 6) `while` Loops

Repeat code while a condition is true:

### Basic `while` loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0, 1, 2, 3, 4
```

### User input loop
```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted")
```

### Loop with counter (prevent infinite loops)
```python
attempts = 0
max_attempts = 3
password = ""

while password != "secret" and attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1

if password == "secret":
    print("Access granted")
else:
    print("Too many attempts")
```

### Rule of thumb
- Always ensure loop condition changes each iteration
- Use counters to prevent infinite loops
- `while` is good when you don't know how many iterations

---

## 7) `for` Loops

Iterate over a sequence (list, string, range, etc.):

### Looping over a list
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry
```

### Looping over a string
```python
word = "Python"
for letter in word:
    print(letter)
# Output: P, y, t, h, o, n
```

### Looping with `range()`
```python
# Range from 0 to 4 (exclusive)
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Range with start and end
for i in range(2, 5):
    print(i)
# Output: 2, 3, 4

# Range with step
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

### Looping with index using `enumerate()`
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```

### Rule of thumb
- Use `for` when you know what you're iterating over
- Use `range()` for numeric sequences
- Use `enumerate()` when you need both index and value

---

## 8) Loop Control: `break` and `continue`

### `break` - Exit loop early
```python
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

### `continue` - Skip to next iteration
```python
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)
# Output: 1, 3, 5, 7, 9
```

### `else` clause with loops
```python
# else runs if loop completes normally (no break)
for i in range(5):
    if i == 10:  # Never true
        break
else:
    print("Loop completed normally")
```

### Rule of thumb
- `break` - exit loop completely
- `continue` - skip current iteration, continue loop
- Use `break` sparingly - prefer clear loop conditions
- `else` with loops is advanced - use when needed

---

## 9) Nested Loops

Loops inside loops:

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Blank line between tables
```

### Rule of thumb
- Nested loops multiply iterations (3x3 = 9 iterations)
- Keep nesting shallow (2-3 levels max)
- Use meaningful variable names (`i`, `j`, `k` is fine for simple cases)

---

## 10) Random Numbers

Use `random` module for randomness:

```python
import random

# Random integer between 1 and 10 (inclusive)
number = random.randint(1, 10)

# Random float between 0 and 1
decimal = random.random()

# Random choice from a list
fruits = ["apple", "banana", "cherry"]
choice = random.choice(fruits)

# Shuffle a list (in place)
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
```

### Common use: Guessing games
```python
import random

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number (1-100): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("You got it!")
```

---

## Common Mistakes + Fixes

- **Mistake**: Infinite `while` loop  
  **Fix**: Ensure loop condition changes each iteration. Use counters.

- **Mistake**: Wrong indentation  
  **Fix**: Python uses indentation for blocks. Use 4 spaces consistently.

- **Mistake**: Comparing string to int  
  **Fix**: Convert inputs first: `int(input(...))`

- **Mistake**: Using `=` instead of `==` in conditions  
  **Fix**: `=` is assignment, `==` is comparison

- **Mistake**: Forgetting colon after `if`/`for`/`while`  
  **Fix**: Always end with `:`: `if condition:`

- **Mistake**: Off-by-one errors with `range()`  
  **Fix**: Remember `range(5)` gives 0-4, not 0-5

- **Mistake**: Modifying list while iterating  
  **Fix**: Iterate over a copy: `for item in list.copy():`

---

## Best Practices

1. **Use clear condition names** - Make conditions readable
   ```python
   # Good
   is_adult = age >= 18
   if is_adult:
       ...
   
   # Avoid
   if age >= 18:
       ...
   ```

2. **Prefer `for` over `while` when possible** - More predictable
   ```python
   # Good - know exactly how many iterations
   for i in range(10):
       ...
   
   # Only use while when condition is dynamic
   while user_input != "quit":
       ...
   ```

3. **Avoid deep nesting** - Flatten with `and`/`or` or extract functions
   ```python
   # Good
   if age >= 18 and has_license:
       ...
   
   # Avoid (too nested)
   if age >= 18:
       if has_license:
           ...
   ```

4. **Use `break` and `continue` sparingly** - Clear loop conditions are better
   ```python
   # Good
   for i in range(10):
       if i % 2 == 0:
           continue
       print(i)
   
   # Better (clearer intent)
   for i in range(1, 10, 2):  # Only odd numbers
       print(i)
   ```

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can write `if/elif/else` branches correctly
- [ ] I can use comparison and logical operators
- [ ] I can build a safe `while` loop with a stop condition
- [ ] I can use `for` loops with `range()` and lists
- [ ] I can use `break` and `continue` intentionally
- [ ] I can handle user input in loops
- [ ] I can use random numbers in simple games
- [ ] My indentation is correct

---

## 60-Second Recap

- **Conditionals branch logic** - `if/elif/else` choose paths
- **Loops repeat logic** - `while` for unknown count, `for` for known sequences
- **Comparison operators** - `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical operators** - `and`, `or`, `not` combine conditions
- **Loop control** - `break` exits, `continue` skips iteration
- **Randomness** - `random.randint()` for games and simulations

---

## Mini Q&A

**Q: When should I use `while` vs `for`?**  
A: `while` when repeating until a condition changes (user input, unknown count). `for` when iterating known items (list, range, string).

**Q: Is nested `if` bad?**  
A: Not always, but keep it readable. Flatten with `and`/`or` when it improves clarity.

**Q: What's the difference between `=` and `==`?**  
A: `=` assigns a value. `==` compares values. Use `==` in conditions.

**Q: Why does `range(5)` give 0-4, not 0-5?**  
A: `range()` is exclusive of the end value (like slicing). Use `range(6)` to get 0-5.

**Q: Can I use `break` in a `while` loop?**  
A: Yes! `break` works in both `for` and `while` loops.

**Q: What does `continue` do?**  
A: Skips the rest of the current iteration and goes to the next one. Loop continues.

**Q: How do I generate random numbers?**  
A: `import random`, then `random.randint(1, 10)` for integers, `random.random()` for floats.

**Q: What's the `else` clause on a loop?**  
A: Runs if the loop completes normally (no `break`). Advanced feature - use when you need it.
