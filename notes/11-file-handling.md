# 11: File Handling - Reading and Writing Files

## Why this matters

Most real programs read from and write to files. Files persist data between program runs and allow data sharing between programs.

Good file handling gives you:
- Persistent data storage
- Data sharing between programs
- Configuration files
- Logging and reporting
- Data import/export

---

## 1) Reading Text Files

### Opening files with `with` statement (recommended)
```python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# File automatically closed when block exits
```

### Why `with` statement?
- **Automatic cleanup** - File closed even if error occurs
- **Cleaner code** - No need to remember `file.close()`
- **Exception safe** - Handles errors gracefully

### Reading methods
```python
with open("data.txt", "r") as file:
    # Read entire file as string
    content = file.read()
    
    # Read one line
    line = file.readline()
    
    # Read all lines as list
    lines = file.readlines()
    
    # Iterate line by line (memory efficient)
    for line in file:
        print(line.strip())  # strip() removes newline
```

### File modes
- `"r"` - Read (default for text files)
- `"w"` - Write (overwrites existing file)
- `"a"` - Append (adds to end of file)
- `"r+"` - Read and write
- `"x"` - Exclusive creation (fails if file exists)

### Rule of thumb
- Always use `with open()` - automatic cleanup
- Use `read()` for small files
- Use iteration (`for line in file:`) for large files
- Remember to strip newlines: `line.strip()`

---

## 2) Writing Text Files

### Writing to files
```python
# Write mode (overwrites existing file)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Append mode (adds to end)
with open("log.txt", "a") as file:
    file.write("New log entry\n")
```

### Writing multiple lines
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("output.txt", "w") as file:
    file.writelines(lines)

# Or write each line
with open("output.txt", "w") as file:
    for line in lines:
        file.write(line)
```

### Important notes
- `write()` doesn't add newlines automatically
- Use `\n` for newlines
- `"w"` mode overwrites existing files
- `"a"` mode appends to existing files

### Rule of thumb
- Use `"w"` when you want to replace file contents
- Use `"a"` when you want to add to existing file
- Always add `\n` for newlines in `write()`
- Be careful with `"w"` - it deletes existing content!

---

## 3) Working with CSV Files

CSV (Comma-Separated Values) is common for tabular data.

### Reading CSV files
```python
import csv

# Using csv.reader (returns lists)
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list

# Using csv.DictReader (returns dictionaries) - PREFERRED
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])  # Access by column name
        print(row["age"])
```

### CSV file example
```csv
name,age,city
Alice,25,Edinburgh
Bob,30,London
```

### Writing CSV files
```python
import csv

# Using csv.writer
data = [
    ["name", "age", "city"],
    ["Alice", "25", "Edinburgh"],
    ["Bob", "30", "London"],
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Using csv.DictWriter - PREFERRED
data = [
    {"name": "Alice", "age": "25", "city": "Edinburgh"},
    {"name": "Bob", "age": "30", "city": "London"},
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write column names
    writer.writerows(data)
```

### Important: `newline=""` parameter
```python
# Always use newline="" when writing CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # ...
```

### Rule of thumb
- Use `csv.DictReader`/`csv.DictWriter` - column names make code clearer
- Always use `newline=""` when writing CSV files
- CSV values are strings - convert to numbers if needed
- Use `DictReader`/`DictWriter` for readability

---

## 4) Working with JSON Files

JSON (JavaScript Object Notation) is common for structured data.

### Reading JSON files
```python
import json

with open("data.json", "r") as file:
    data = json.load(file)  # Loads entire file
    print(data["name"])
    print(data["age"])
```

### Writing JSON files
```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "Edinburgh"
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=2)  # indent for readability
```

### JSON string conversion
```python
import json

# Convert Python object to JSON string
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
# Result: '{"name": "Alice", "age": 25}'

# Convert JSON string to Python object
python_obj = json.loads(json_string)
# Result: {"name": "Alice", "age": 25}
```

### Rule of thumb
- Use `json.load()` to read from file
- Use `json.dump()` to write to file
- Use `json.loads()` for JSON strings
- Use `json.dumps()` to create JSON strings
- Use `indent=2` for readable JSON files

---

## 5) Files and Classes

Common pattern: Load data from files into class instances:

### Loading CSV into objects
```python
import csv

class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = int(year)
        self.rating = float(rating)
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.rating}/10"

def load_movies(filename):
    movies = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie = Movie(
                row["title"],
                row["year"],
                row["rating"]
            )
            movies.append(movie)
    return movies

# Use it
movies = load_movies("movies.csv")
for movie in movies:
    print(movie)
```

### Saving objects to files
```python
def save_movies(movies, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "year", "rating"])
        writer.writeheader()
        for movie in movies:
            writer.writerow({
                "title": movie.title,
                "year": movie.year,
                "rating": movie.rating
            })
```

### Rule of thumb
- Load file data into class instances for better organization
- Convert types when loading (CSV values are strings)
- Create helper methods like `to_dict()` for saving

---

## 6) File Paths and Error Handling

### File paths
```python
# Relative path (from current directory)
with open("data.txt", "r") as file:
    ...

# Absolute path
with open("/Users/username/data.txt", "r") as file:
    ...

# Path with os.path (cross-platform)
import os
path = os.path.join("folder", "subfolder", "file.txt")
```

### Checking if file exists
```python
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as file:
        ...
else:
    print("File not found")
```

### Handling file errors
```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Error: {e}")
```

### Rule of thumb
- Use relative paths when possible
- Check file existence with `os.path.exists()` if needed
- Handle `FileNotFoundError` for missing files
- Handle `PermissionError` for access issues

---

## 7) Common Patterns

### Reading and processing
```python
def process_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                process_line(line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found")
```

### Appending to log file
```python
def log_message(message):
    with open("app.log", "a") as file:
        file.write(f"{datetime.now()}: {message}\n")
```

### Reading configuration
```python
import json

def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Default empty config
```

---

## Common Mistakes + Fixes

- **Mistake**: Forgetting to close file handles  
  **Fix**: Always use `with open()` - automatic cleanup

- **Mistake**: Accidentally overwriting data with `"w"`  
  **Fix**: Use `"a"` when appending, `"w"` only when replacing

- **Mistake**: Treating CSV numbers as ints automatically  
  **Fix**: Convert explicitly: `int(row["age"])` or `float(row["price"])`

- **Mistake**: Wrong field names in `DictWriter`  
  **Fix**: Match headers exactly - check `fieldnames` parameter

- **Mistake**: Forgetting `newline=""` with CSV  
  **Fix**: Always use `newline=""` when writing CSV files

- **Mistake**: Not handling `FileNotFoundError`  
  **Fix**: Wrap file operations in try/except

- **Mistake**: Reading entire large file into memory  
  **Fix**: Use iteration (`for line in file:`) for large files

---

## Best Practices

1. **Always use `with` statement**
   ```python
   # Good
   with open("file.txt", "r") as file:
       content = file.read()
   
   # Avoid
   file = open("file.txt", "r")
   content = file.read()
   file.close()  # Easy to forget!
   ```

2. **Use appropriate file mode**
   ```python
   # Good - clear intent
   with open("log.txt", "a") as file:  # Append
       file.write("New entry\n")
   
   with open("output.txt", "w") as file:  # Replace
       file.write("New content\n")
   ```

3. **Handle file errors**
   ```python
   # Good
   try:
       with open("data.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found")
   ```

4. **Use `DictReader`/`DictWriter` for CSV**
   ```python
   # Good - readable
   reader = csv.DictReader(file)
   for row in reader:
       print(row["name"])
   
   # Avoid - unclear
   reader = csv.reader(file)
   for row in reader:
       print(row[0])  # What is index 0?
   ```

5. **Convert types when loading**
   ```python
   # Good - explicit conversion
   age = int(row["age"])
   price = float(row["price"])
   
   # Avoid - string operations on numbers
   total = row["price"] * row["quantity"]  # Error!
   ```

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can read text files using `with open()`
- [ ] I can choose correct file mode (`r`, `w`, `a`)
- [ ] I can read/write CSV with `DictReader`/`DictWriter`
- [ ] I can export JSON from Python data
- [ ] I can map file rows into class instances
- [ ] I handle `FileNotFoundError` appropriately
- [ ] I use `newline=""` when writing CSV files
- [ ] I convert CSV string values to appropriate types

---

## 60-Second Recap

- **File IO is essential** - Persistent data storage
- **Always use `with open()`** - Automatic cleanup
- **CSV and JSON are common formats** - Learn both
- **Context managers make file handling safer** - `with` statement
- **Handle file errors** - `FileNotFoundError`, `PermissionError`
- **Convert types when loading** - CSV values are strings
- **Use `DictReader`/`DictWriter`** - Column names improve readability

---

## Mini Q&A

**Q: Why use `with open(...)`?**  
A: It guarantees file cleanup/close, even if an error occurs. Safer than manual `close()`.

**Q: CSV row types are always correct?**  
A: No - CSV usually reads values as strings. Convert explicitly: `int(row["age"])`.

**Q: What's the difference between `"w"` and `"a"` modes?**  
A: `"w"` overwrites existing file. `"a"` appends to existing file.

**Q: Do I need to close files with `with` statement?**  
A: No - `with` automatically closes files when block exits.

**Q: How do I read a file line by line?**  
A: Use iteration: `for line in file:` or `file.readline()` in a loop.

**Q: What's `newline=""` for in CSV writing?**  
A: Prevents extra blank lines between rows. Always use it with CSV writing.

**Q: Can I read JSON and CSV the same way?**  
A: No - use `json.load()` for JSON, `csv.DictReader()` for CSV.

**Q: How do I check if a file exists?**  
A: Use `os.path.exists("filename")` or handle `FileNotFoundError` exception.
