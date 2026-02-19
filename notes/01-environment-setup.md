# 01: Environment Setup and Getting Started with Python

## Why this matters

This is the foundation for everything else in the course. Understanding how to set up your development environment and run Python programs is essential.

Good setup gives you:
- Isolated project dependencies
- Proper IDE configuration
- Working Python environment
- Ability to run and test code
- Understanding of Python execution
- Foundation for all future learning

---

## 1) Setting Up Your Python Environment

### Verify Python Installation
```bash
# Check Python version
python --version
# or
python3 --version

# Expected: Python 3.11.x or higher

# Verify pip is installed
pip --version
# or
pip3 --version
```

### Create Virtual Environment
```bash
# Create project directory
mkdir python-training
cd python-training

# Create virtual environment
python -m venv venv
# or
python3 -m venv venv
```

### Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Verify activation (you should see (venv) in prompt)
which python   # macOS/Linux
where python   # Windows
```

### Install Dependencies
```bash
# Create requirements.txt
# pytest>=7.0.0
# requests>=2.28.0

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### Rule of thumb
- Always use virtual environments for projects
- Activate venv before working on project
- Use `requirements.txt` to track dependencies
- Virtual environments isolate project dependencies

---

## 2) Your First Python Program

### Creating a Python file
```python
# hello.py
print("Hello, World!")
```

### Running Python files
```bash
# From terminal/command line
python hello.py

# Or with Python 3 explicitly
python3 hello.py
```

### Key idea
- Python files have `.py` extension
- `print()` outputs text to console
- Python executes code top-to-bottom
- `print()` is your first debugging tool

---

## 3) The Python Execution Model

### How Python runs code
```python
# Python executes line by line, top to bottom
print("First")
print("Second")
print("Third")

# Output:
# First
# Second
# Third
```

### Execution flow
1. Python reads the file
2. Executes statements in order
3. Outputs results to console
4. Program ends

### Rule of thumb
- Code runs sequentially
- Each line executes before the next
- Output appears immediately when `print()` runs

---

## 4) Using `print()` for Output

### Basic printing
```python
print("Hello, World!")
print(42)
print(3.14)
```

### Printing multiple items
```python
print("Hello", "World")  # Multiple arguments
print("Name:", "Alice", "Age:", 25)
```

### Printing variables
```python
name = "Alice"
age = 25
print(name)
print(age)
print("Name:", name, "Age:", age)
```

### Formatting output
```python
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")  # f-string (we'll learn more later)
```

### Rule of thumb
- `print()` displays output to console
- Use `print()` to see what your program is doing
- `print()` is essential for debugging

---

## 5) The Run-Check-Improve Loop

### Development workflow
1. **Edit code** - Write or modify Python code
2. **Run file** - Execute with `python filename.py`
3. **Read output/error** - See what happened
4. **Fix and rerun** - Make changes and test again

### Example cycle
```python
# Step 1: Write code
print("Hello")

# Step 2: Run it
# Output: Hello

# Step 3: Improve
print("Hello, World!")

# Step 4: Run again
# Output: Hello, World!
```

### Rule of thumb
- Small edit/run cycles build confidence
- Test frequently - don't write everything then run
- Read error messages carefully - they tell you what's wrong

---

## 6) Reading Error Messages

### Common error format
```python
# Code with error
print("Hello"  # Missing closing parenthesis

# Error message:
# SyntaxError: unexpected EOF while parsing
```

### Understanding errors
- **Error type** - What went wrong (`SyntaxError`, `NameError`, etc.)
- **Error message** - Description of the problem
- **Line number** - Where the error occurred

### Example errors
```python
# NameError - variable doesn't exist
print(undefined_variable)
# NameError: name 'undefined_variable' is not defined

# SyntaxError - invalid syntax
print("Hello"
# SyntaxError: unexpected EOF while parsing
```

### Rule of thumb
- Read error messages carefully
- Check the line number mentioned
- Common errors: typos, missing quotes, missing parentheses
- Don't panic - errors are learning opportunities!

---

## 7) Python File Structure

### Basic file structure
```python
# Comments start with #
# They explain what code does

# Import statements (we'll learn later)
# import something

# Your code here
print("Hello, World!")
```

### File naming
- Use `.py` extension: `hello.py`, `my_program.py`
- Use lowercase with underscores: `my_program.py` (not `MyProgram.py`)
- Avoid spaces: `my_program.py` (not `my program.py`)

### Rule of thumb
- Keep filenames descriptive but short
- Use lowercase with underscores
- Always use `.py` extension

---

## 8) Comments in Python

### Single-line comments
```python
# This is a comment
print("Hello")  # Comment at end of line

# Comments are ignored by Python
# They help explain your code
```

### Multi-line comments
```python
"""
This is a multi-line comment
or docstring (we'll learn more later)
It can span multiple lines
"""

print("Hello")
```

### Rule of thumb
- Use comments to explain why, not what
- Comments help others (and future you) understand code
- Don't over-comment obvious code

---

## Common Mistakes + Fixes

- **Mistake**: Nothing prints  
  **Fix**: Check you're running the right file. Verify file path in command.

- **Mistake**: Typo in `print`  
  **Fix**: Verify spelling and brackets: `print()` not `prnt()` or `print(`

- **Mistake**: Edited one file, ran another  
  **Fix**: Double-check the path in your command matches the file you edited.

- **Mistake**: Forgetting quotes around strings  
  **Fix**: Strings need quotes: `print("Hello")` not `print(Hello)`

- **Mistake**: Missing closing parenthesis  
  **Fix**: Every `(` needs a matching `)`: `print("Hello")`

- **Mistake**: Running wrong Python version  
  **Fix**: Use `python3` if `python` points to Python 2 (rare now)

---

## Best Practices

1. **Test frequently**
   ```python
   # Good - test as you go
   print("Hello")
   # Run it, see output, then continue
   
   # Avoid - writing everything then running
   # 100 lines of code...
   # Now run and hope it works
   ```

2. **Use descriptive filenames**
   ```python
   # Good
   hello_world.py
   user_input.py
   
   # Avoid
   test.py
   stuff.py
   ```

3. **Read error messages**
   ```python
   # Good - read the error, understand it, fix it
   # Error: SyntaxError: unexpected EOF
   # Fix: Missing closing parenthesis
   
   # Avoid - ignore errors and guess
   ```

4. **Use comments wisely**
   ```python
   # Good - explains why
   # Calculate total with 20% tax
   total = price * 1.20
   
   # Avoid - states the obvious
   # Set price to 100
   price = 100
   ```

---

## Quick Lab Checklist

Before moving on, verify:

- [ ] I can create a `.py` file
- [ ] I can run Python files from terminal
- [ ] I can use `print()` to display output
- [ ] I can read and understand error messages
- [ ] I understand Python executes top-to-bottom
- [ ] I can fix simple syntax errors

---

## 60-Second Recap

- **Python files are plain text** - `.py` extension
- **`print()` gives immediate feedback** - Essential for debugging
- **Code runs top-to-bottom** - Sequential execution
- **Small edit/run cycles** - Build confidence fast
- **Read error messages** - They tell you what's wrong
- **Test frequently** - Don't write everything then run

---

## Mini Q&A

**Q: Do I need an IDE to run Python?**  
A: No - terminal + Python is enough. But IDEs make development easier.

**Q: Why start with `print()`?**  
A: It confirms your code actually ran and shows values. Essential for debugging.

**Q: What if my program doesn't run?**  
A: Check the error message. Common issues: typos, missing quotes, wrong file path.

**Q: Can I run Python code without saving to a file?**  
A: Yes - use Python REPL (interactive mode): `python` then type code. But files are better for programs.

**Q: What's the difference between `python` and `python3`?**  
A: `python3` explicitly uses Python 3. `python` might point to Python 2 (rare now). Use `python3` if unsure.

**Q: How do I stop a running program?**  
A: Press `Ctrl+C` (or `Cmd+C` on Mac) in the terminal.

**Q: Can I run Python files from anywhere?**  
A: Yes - use full path or navigate to file directory first: `cd /path/to/file` then `python file.py`.

**Q: Why use virtual environments?**  
A: They isolate project dependencies. Different projects can use different package versions without conflicts.

**Q: How do I deactivate a virtual environment?**  
A: Type `deactivate` in the terminal. The `(venv)` prefix will disappear from your prompt.

**Q: Do I need to activate venv every time?**  
A: Yes - activate it each time you start working on the project. Your IDE may do this automatically.

**Q: What's the difference between `python` and `python3`?**  
A: `python3` explicitly uses Python 3. `python` might point to Python 2 (rare now). Use `python3` if unsure.
