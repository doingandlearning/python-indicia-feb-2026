# 09: Exception Handling - Robust Error Management

## Why this matters

Good exception handling keeps applications robust and user-friendly. Programs crash gracefully instead of showing cryptic errors, and users get helpful messages.

Good exception handling gives you:
- Graceful error recovery
- Better user experience
- Easier debugging
- Robust applications
- Clear error messages

---

## 1) What Are Exceptions?

Exceptions are runtime errors that interrupt normal program flow:

### Common exceptions
```python
# ValueError - wrong value type
int("not a number")  # ValueError: invalid literal

# TypeError - wrong type operation
"hello" + 5  # TypeError: can only concatenate str

# KeyError - missing dictionary key
person = {"name": "Alice"}
person["age"]  # KeyError: 'age'

# IndexError - list index out of range
items = [1, 2, 3]
items[10]  # IndexError: list index out of range

# FileNotFoundError - file doesn't exist
open("missing.txt")  # FileNotFoundError
```

### What happens without handling
```python
age = int(input("Enter age: "))  # User types "twenty"
# Program crashes with: ValueError: invalid literal for int()
```

---

## 2) Handling Errors with `try/except`

### Basic try/except
```python
try:
    age = int(input("Enter age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number")
```

### How it works
```python
try:
    # Risky code that might raise exception
    risky_operation()
except ExceptionType:
    # What to do if exception occurs
    handle_error()
```

### Multiple exception types
```python
try:
    number = int(input("Enter number: "))
    result = 10 / number
except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Catching multiple exceptions
```python
try:
    # Risky code
    pass
except (ValueError, TypeError):
    # Handle both ValueError and TypeError
    print("Invalid value or type")
```

### Rule of thumb
- `try` - code that might raise exception
- `except` - handles specific exception types
- Catch specific exceptions first, then general ones
- One `try` can have multiple `except` blocks

---

## 3) The `else` Clause

Runs if no exception occurred:

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid number")
else:
    # Only runs if no exception
    print(f"Age entered successfully: {age}")
```

### Rule of thumb
- `else` runs when `try` block completes without exceptions
- Use `else` for code that should only run on success
- Less common than `except`, but useful

---

## 4) The `finally` Clause

Always runs, regardless of exceptions:

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # Always runs - even if exception occurs
    file.close()  # Ensure file is closed
```

### Common use: Cleanup
```python
try:
    # Do something
    process_data()
except Exception:
    # Handle error
    log_error()
finally:
    # Always cleanup
    cleanup_resources()
```

### Rule of thumb
- `finally` always executes
- Use for cleanup (closing files, releasing resources)
- `finally` runs even if `return` is in `try` or `except`

---

## 5) Raising Exceptions Intentionally

Raise exceptions when business rules are violated:

### Basic `raise`
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")  # Error: Age cannot be negative
```

### Raising with message
```python
if condition:
    raise ValueError("Descriptive error message")
```

### Re-raising exceptions
```python
try:
    risky_operation()
except ValueError:
    # Log error, then re-raise
    print("Error occurred")
    raise  # Re-raise the same exception
```

### Rule of thumb
- Raise exceptions for exceptional states (errors)
- Use clear, descriptive error messages
- Raise early - validate inputs at function boundaries
- Don't use exceptions for normal control flow

---

## 6) Custom Exceptions

Create domain-specific exceptions:

### Simple custom exception
```python
class EmailAlreadyExists(Exception):
    """Raised when email already exists in system."""
    pass

# Use it
def register_user(email):
    if email_exists(email):
        raise EmailAlreadyExists(f"Email {email} already registered")
    # Register user...
```

### Custom exception with data
```python
class ValidationError(Exception):
    """Raised when validation fails."""
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(self.message)

# Use it
def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative", "age")
```

### Rule of thumb
- Create custom exceptions for domain-specific errors
- Inherit from `Exception` (or more specific exception)
- Add helpful attributes if needed
- Use clear, descriptive names

---

## 7) Exception Hierarchy

Python exceptions form a hierarchy:

```
BaseException
├── Exception
    ├── ValueError
    ├── TypeError
    ├── KeyError
    ├── IndexError
    ├── FileNotFoundError
    └── ... (many more)
```

### Catching base exceptions
```python
try:
    risky_operation()
except Exception:  # Catches all exceptions
    print("Something went wrong")
```

### Rule of thumb
- Catch specific exceptions first
- Use `Exception` as fallback (not `BaseException`)
- More specific = better error handling

---

## 8) Common Patterns

### Input validation pattern
```python
def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0:
                raise ValueError("Age cannot be negative")
            return age
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
```

### File handling pattern
```python
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"Permission denied for {filename}")
        return None
```

### Dictionary access pattern
```python
# Using .get() (preferred)
value = data.get("key", default_value)

# Using try/except
try:
    value = data["key"]
except KeyError:
    value = default_value
```

### Rule of thumb
- Validate inputs at function boundaries
- Use `with` statement for file handling (automatic cleanup)
- Prefer `.get()` for dictionary access when default is acceptable
- Use try/except when you need specific error handling

---

## 9) Best Practices

### 1. Be specific
```python
# Good - specific exception
try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid number")

# Avoid - too broad
try:
    age = int(input("Age: "))
except:  # Catches everything - bad!
    print("Error")
```

### 2. Don't suppress exceptions silently
```python
# Good - log or inform user
try:
    risky_operation()
except ValueError as e:
    print(f"Error: {e}")

# Avoid - silent failure
try:
    risky_operation()
except:
    pass  # User never knows what went wrong!
```

### 3. Raise early, handle late
```python
# Good - validate early
def process_order(order):
    if not order.items:
        raise ValueError("Order must have items")
    # Process order...

# Avoid - validate late
def process_order(order):
    # Process order...
    if not order.items:  # Too late!
        return None
```

### 4. Use exceptions for exceptional cases
```python
# Good - exception for error
if age < 0:
    raise ValueError("Age cannot be negative")

# Avoid - exception for normal flow
try:
    result = find_item(item)
except NotFoundError:  # Not really exceptional
    return None
```

---

## Common Mistakes + Fixes

- **Mistake**: Catching broad `Exception` first  
  **Fix**: Catch specific exceptions first, then general fallback

- **Mistake**: Returning error strings instead of raising  
  **Fix**: Use exceptions for exceptional states: `raise ValueError("message")`

- **Mistake**: Silent except blocks  
  **Fix**: Log and/or message appropriately: `except ValueError as e: print(e)`

- **Mistake**: Catching exception but not handling  
  **Fix**: Either handle it properly or let it propagate

- **Mistake**: Using exceptions for normal control flow  
  **Fix**: Use if/else for normal flow, exceptions for errors

- **Mistake**: Bare `except:` clause  
  **Fix**: Always specify exception type: `except ValueError:`

- **Mistake**: Not cleaning up resources  
  **Fix**: Use `finally` or `with` statement for cleanup

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can identify common exception types (`ValueError`, `TypeError`, `KeyError`, etc.)
- [ ] I can use `try/except` for risky operations
- [ ] I can raise `ValueError` with clear messages
- [ ] I can create a custom exception class
- [ ] I understand when to use `else` and `finally`
- [ ] I catch specific exceptions before general ones
- [ ] I don't suppress exceptions silently

---

## 60-Second Recap

- **Exceptions separate error handling** - Keep normal logic clean
- **`try/except` handles errors** - Catch and handle gracefully
- **Specific catches improve clarity** - Catch `ValueError` before `Exception`
- **Raise exceptions for errors** - Use clear, descriptive messages
- **Custom exceptions improve domain modeling** - Create domain-specific errors
- **`finally` ensures cleanup** - Always runs, even if exception occurs
- **Don't use exceptions for normal flow** - Use if/else for normal cases

---

## Mini Q&A

**Q: Should I wrap all code in `try`?**  
A: No - only wrap risky operations (user input, file operations, network calls).

**Q: Return error string or raise exception?**  
A: Raise exception for true error states. Return values for normal flow.

**Q: What's the difference between `except:` and `except Exception:`?**  
A: `except:` catches everything (including system exits). `except Exception:` catches normal exceptions (preferred).

**Q: Can I have multiple `except` blocks?**  
A: Yes - catch different exception types separately for specific handling.

**Q: What does `raise` without arguments do?**  
A: Re-raises the current exception (useful in exception handlers).

**Q: Should I catch `Exception` or specific types?**  
A: Catch specific types when possible. Use `Exception` as fallback only.

**Q: When should I create custom exceptions?**  
A: When you need domain-specific errors that make code more readable and maintainable.

**Q: What's the difference between `except ValueError:` and `except ValueError as e:`?**  
A: `as e` gives you access to the exception object (for error messages, attributes, etc.).
