# 10: Modules & Packages

## Why this matters

Good organization gives you:

- Reusable code
- Easier testing
- Easier debugging
- Cleaner files
- Better teamwork

---

## 1) Module Basics

## What is a module?

A **module** is just a single Python file (`.py`) with related code.

Example module:

```python
# user_validation.py
"""User validation functions."""

def validate_email(email):
    return bool(email) and "@" in email

def validate_name(name):
    return bool(name and name.strip())
```

Use it:

```python
import user_validation

print(user_validation.validate_email("alice@example.com"))
```

### Rule of thumb

- One module = one concern (validation, reporting, etc.)

---

## 2) First Module You Can Build

```python
# user_functions.py
"""User management functions."""

users = []

def add_user(name, email, role="user"):
    user = {"name": name, "email": email, "role": role}
    users.append(user)
    return user

def find_user_by_email(email):
    for user in users:
        if user["email"] == email:
            return user
    return None

def list_users():
    return users.copy()
```

Use it:

```python
import user_functions

user_functions.add_user("Alice", "alice@example.com", "admin")
print(user_functions.find_user_by_email("alice@example.com"))
```

---

## 3) Import Styles (Know these for lab)

### A. Import whole module (most explicit)

```python
import user_functions
user_functions.add_user("Alice", "alice@example.com")
```

### B. Import specific names

```python
from user_functions import add_user, find_user_by_email
add_user("Alice", "alice@example.com")
```

### C. Alias module

```python
import user_functions as uf
uf.add_user("Alice", "alice@example.com")
```

### D. Alias individual names

```python
from user_functions import add_user as add
add("Alice", "alice@example.com")
```

### E. Wildcard import (avoid)

```python
from user_functions import *
```

Why avoid: unclear origin + name collisions.

### Quick decision guide

- Prefer `import module` for clarity and fewer conflicts.
- Use `from module import name` when you need only a few functions.
- Avoid `import *`.

---

## 4) Python Standard Library, PyPI, and pip

### Python Standard Library (built in)

These modules ship with Python, so you **do not** install them with pip.

Official docs: https://docs.python.org/3/library/

Learning tip: use the official docs to see what is available, then pair that with an LLM to ask for plain-English explanations, examples, and comparisons between similar modules.

```python
import math
import random
import datetime

print(math.sqrt(16))
print(random.randint(1, 10))
print(datetime.datetime.now())
```

### PyPI (Python Package Index)

PyPI is the public package registry for Python packages (third-party libraries).

- Standard library = built into Python
- PyPI packages = installed separately

### Install packages with `pip install`

Install one package:

```bash
pip install requests
```

Install all required packages from file:

```bash
pip install -r requirements.txt
```

### Save current environment with `pip freeze`

Show installed packages + versions:

```bash
pip freeze
```

Save to requirements file:

```bash
pip freeze > requirements.txt
```

Tip: do installs/freezes inside your virtual environment for clean project dependencies.

---

## 5) Module Properties You Should Recognize

```python
import user_functions

print(user_functions.__name__)  # module name
print(user_functions.__file__)  # file path
print(user_functions.__doc__)   # module docstring
print(dir(user_functions))      # all names in module
```

Useful exploration pattern:

```python
public = [name for name in dir(user_functions) if not name.startswith("_")]
print(public)
```

---

## 6) `if __name__ == "__main__"` Pattern

Use this to run test/demo code only when file runs directly.

```python
def add_user(name, email):
    print(f"Added {name}")

if __name__ == "__main__":
    print("Testing user module")
    add_user("Test User", "test@example.com")
```

### Behavior

- Run file directly: block executes
- Import module elsewhere: block does **not** execute

---

## 7) Package Basics

## What is a package?

A **package** is a folder of modules (typically with `__init__.py`).

Example structure:

```text
user_management/
├── __init__.py
├── user_functions.py
├── user_validation.py
└── user_reporting.py
```

### Why packages?

- Group related modules
- Better project structure
- Easier imports and scaling

---

## 8) `__init__.py` Essentials

`__init__.py` can be empty, but often exposes top-level API:

```python
# user_management/__init__.py
from .user_functions import add_user, find_user_by_email
from .user_validation import validate_email, validate_name

__version__ = "1.0.0"

__all__ = [
    "add_user",
    "find_user_by_email",
    "validate_email",
    "validate_name",
]
```

This allows:

```python
import user_management
user_management.add_user("Alice", "alice@example.com")
```

---

## 9) Relative vs Absolute Imports

Inside a package, prefer relative imports.

### Relative (inside same package)

```python
from .user_functions import add_user
from .user_validation import validate_email
```

### Absolute

```python
from user_management.user_functions import add_user
```

### Rule

- **Inside package modules**: relative imports are usually cleaner.
- **From outside package**: absolute imports are usually clearer.

---

## 10) Common Mistakes + Fixes

- **Mistake**: everything in one giant file  
  **Fix**: split by concern (validation/functions/reporting)

- **Mistake**: `from module import *`  
  **Fix**: explicit imports

- **Mistake**: forgetting `__init__.py` in package folder  
  **Fix**: add `__init__.py`

- **Mistake**: wrong internal import path  
  **Fix**: use `from .module import name` inside package

- **Mistake**: demo/test code runs on import  
  **Fix**: wrap in `if __name__ == "__main__":`

- **Mistake**: trying `pip install math` (or other stdlib modules)  
  **Fix**: standard library modules are built in; only install third-party packages from PyPI

---

## 11) Organization Best Practices

- Keep modules focused: one responsibility each.
- Use clear names (`user_validation.py`, not `stuff.py`).
- Add module docstrings.
- Keep public API clean in `__init__.py`.
- Return copies of mutable shared data when needed.

---

## Quick Lab Checklist

Before submission, verify:

- [ ] Code is split into logical modules
- [ ] Package directory has `__init__.py`
- [ ] Imports are explicit and readable
- [ ] Internal package imports use correct relative form
- [ ] No unnecessary wildcard imports
- [ ] Optional test/demo code is under `if __name__ == "__main__":`
- [ ] Third-party dependencies are installed with `pip install -r requirements.txt`
- [ ] Dependencies are captured with `pip freeze > requirements.txt` when needed

---

## 60-Second Recap

- **Module** = one `.py` file with related code.
- **Package** = directory of modules (with `__init__.py`).
- Python ships with a **standard library** (no pip install needed).
- **PyPI** is where third-party libraries come from.
- Main import styles: `import module`, `from module import name`, aliasing.
- Use `pip install` to add packages and `pip freeze` to capture exact versions.
- Use `if __name__ == "__main__":` for direct-run code only.
- Use relative imports (`from .x import y`) within package modules.
- Good organization now saves lots of debugging time later.

---

## Mini Q&A

**Q: Module vs package?**  
A: Module = file. Package = directory of modules.

**Q: Do I need `__init__.py`?**  
A: In this training context, yes—include it.

**Q: Should I use `from x import *`?**  
A: Usually no.

**Q: Do I pip install standard library modules like `math` or `random`?**  
A: No. Those are built into Python.

**Q: What is `pip freeze` for?**  
A: It outputs exact installed package versions, usually saved into `requirements.txt` for reproducible environments.

**Q: When does `if __name__ == "__main__"` run?**  
A: Only when that file is run directly.
