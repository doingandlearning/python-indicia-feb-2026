# Appendix: Introduction to NumPy and Pandas

## Why this matters

Working with data is a core part of programming. When you have large datasets or need to perform complex calculations, standard Python lists and dictionaries can be slow and verbose.

NumPy and Pandas are powerful libraries that:
- Make data manipulation faster and easier
- Provide efficient operations on large datasets
- Offer built-in statistical and analytical functions
- Handle structured data (like spreadsheets) naturally
- Reduce code complexity for common data tasks

Good data handling gives you:
- Fast processing of thousands of rows
- Easy filtering and analysis
- Built-in statistics and calculations
- Professional data manipulation tools

**Note**: These are optional tools. For small datasets (< 100 rows) or simple operations, standard Python is fine. Use NumPy/Pandas when you need performance or complex analysis.

---

## 1) The Problem: Why Not Just Use Lists?

### Standard Python Approach

**Working with test scores using Python lists:**

```python
# Student test scores
math_scores = [85, 92, 78, 88, 95]
science_scores = [90, 88, 85, 92, 89]

# To add 5 bonus points to each math score:
bonus_math = []
for score in math_scores:
    bonus_math.append(score + 5)

# To calculate average:
avg_math = sum(math_scores) / len(math_scores)

# To add math and science scores together:
total_scores = []
for i in range(len(math_scores)):
    total_scores.append(math_scores[i] + science_scores[i])

# This works, but:
# ❌ Lots of code for simple operations
# ❌ Slow for large datasets (thousands of rows)
# ❌ Easy to make mistakes with loops
# ❌ No built-in statistical functions
```

### Problems with Lists:

- **Verbose**: Requires loops for element-wise operations
- **Slow**: Not optimized for numerical calculations
- **Error-prone**: Easy to introduce bugs in loops
- **Limited**: No built-in statistics or data analysis tools

### The Solution: NumPy and Pandas

- ✅ **Concise code**: Element-wise operations work automatically
- ✅ **Fast performance**: Optimized C code under the hood
- ✅ **Built-in functions**: Statistics, filtering, grouping
- ✅ **Structured data**: Handle tables and mixed data types easily

---

## 2) What is NumPy?

### Understanding NumPy Arrays

**NumPy** (Numerical Python) provides fast, efficient arrays for numerical data.

### Lists vs NumPy Arrays

**Python lists:**
```python
scores = [85, 92, 78, 88, 95]
print(scores)  # [85, 92, 78, 88, 95]
print(type(scores))  # <class 'list'>

# To add 10 to each element:
new_scores = []
for score in scores:
    new_scores.append(score + 10)
```

**NumPy arrays:**
```python
import numpy as np

scores = np.array([85, 92, 78, 88, 95])
print(scores)  # [85 92 78 88 95]  (no commas!)
print(type(scores))  # <class 'numpy.ndarray'>

# To add 10 to each element:
new_scores = scores + 10  # No loop needed!
print(new_scores)  # [95 102 88 98 105]
```

### Key Differences:

- **Visual**: Arrays print without commas: `[85 92 78]` vs lists `[85, 92, 78]`
- **Operations**: Element-wise operations work automatically
- **Performance**: Much faster for numerical operations
- **Type**: Fixed data type (more memory efficient)

---

## 3) Creating NumPy Arrays

### Installation

```bash
pip install numpy
```

### Creating Arrays

**Method 1: From Python list**
```python
import numpy as np

scores = np.array([85, 92, 78, 88, 95])
print(scores)
```

**Method 2: Using `np.arange()`**
```python
# Similar to range(), but creates an array
numbers = np.arange(0, 10)  # [0 1 2 3 4 5 6 7 8 9]
numbers = np.arange(5, 15)  # [5 6 7 8 9 10 11 12 13 14]
numbers = np.arange(0, 20, 2)  # [0 2 4 6 8 10 12 14 16 18]
```

**Method 3: Using `np.linspace()`**
```python
# Evenly spaced values (includes both endpoints)
values = np.linspace(0, 100, 5)  # [0. 25. 50. 75. 100.]
# Creates 5 evenly spaced values from 0 to 100
```

**Method 4: Special arrays**
```python
zeros = np.zeros(5)  # [0. 0. 0. 0. 0.]
ones = np.ones(5)    # [1. 1. 1. 1. 1.]
```

### Key Points:

- `np.array()` converts lists to arrays
- `np.arange()` creates sequences (like `range()`)
- `np.linspace()` creates evenly spaced values
- Arrays display without commas

---

## 4) NumPy Array Operations

### Element-wise Operations

Operations work automatically on all elements:

```python
import numpy as np

math_scores = np.array([85, 92, 78, 88, 95])
science_scores = np.array([90, 88, 85, 92, 89])

# Addition (element-wise)
total_scores = math_scores + science_scores
print(total_scores)  # [175 180 163 180 184]

# Multiplication by scalar
bonus_scores = math_scores * 1.1  # 10% increase
print(bonus_scores)  # [93.5 101.2 85.8 96.8 104.5]

# Subtraction
difference = science_scores - math_scores
print(difference)  # [5 -4 7 4 -6]

# Division
ratio = science_scores / math_scores
print(ratio)  # [1.059 0.957 1.090 1.045 0.937]
```

### Statistical Functions

```python
import numpy as np

scores = np.array([85, 92, 78, 88, 95])

# Built-in statistics
print(f"Sum: {np.sum(scores)}")      # 438
print(f"Mean: {np.mean(scores):.2f}")  # 87.60
print(f"Max: {np.max(scores)}")       # 95
print(f"Min: {np.min(scores)}")       # 78
print(f"Std Dev: {np.std(scores):.2f}")  # 6.50

# Alternative: using array methods
print(f"Sum: {scores.sum()}")
print(f"Mean: {scores.mean():.2f}")
print(f"Max: {scores.max()}")
print(f"Min: {scores.min()}")
```

### Key Points:

- Operations work element-wise automatically
- No loops needed for basic math
- Use `np.function()` or `array.method()` for statistics
- Both approaches work (choose what's clearer)

---

## 5) Reading CSV Files with NumPy

### Loading Numerical Data

```python
import numpy as np

# Read CSV file (numerical data only)
data = np.loadtxt('scores.csv', delimiter=',')

print(data)
# [[85. 90. 82.]
#  [92. 88. 90.]
#  [78. 85. 80.]]

print(f"Shape: {data.shape}")  # (3, 3) - 3 rows, 3 columns
```

### Working with 2D Arrays

```python
import numpy as np

data = np.loadtxt('scores.csv', delimiter=',')

# Access rows
first_row = data[0]      # [85. 90. 82.]
second_row = data[1]     # [92. 88. 90.]

# Access columns
first_column = data[:, 0]  # All rows, column 0
second_column = data[:, 1]  # All rows, column 1

# Calculate statistics per row
for i, row in enumerate(data):
    print(f"Row {i+1}: Sum={row.sum()}, Mean={row.mean():.2f}")

# Calculate statistics per column
for i in range(data.shape[1]):
    col = data[:, i]
    print(f"Column {i+1}: Mean={col.mean():.2f}")
```

### Key Points:

- `np.loadtxt()` reads numerical CSV files
- Result is a 2D array (rows and columns)
- Use indexing: `data[row, col]` or `data[row][col]`
- Slicing: `data[:, 0]` gets all rows of column 0

---

## 6) What is Pandas?

### Understanding DataFrames

**Pandas** provides DataFrames - like Excel spreadsheets in Python.

### Why Pandas Over NumPy?

**NumPy is great for numbers, but:**
- Column names are lost
- Mixed data types are awkward
- Filtering by name is difficult
- No built-in grouping/aggregation

**Pandas makes structured data easy:**
```python
import pandas as pd

# Read CSV with column names preserved
df = pd.read_csv('students.csv')

# Access columns by name
print(df['student'])  # All student names
print(df['math'].mean())  # Average math score

# Filter easily
high_scores = df[df['math'] > 85]  # Rows where math > 85
```

### DataFrames vs NumPy Arrays:

- **DataFrames**: Tables with column names, mixed types, data analysis
- **NumPy Arrays**: Pure numerical arrays, mathematical operations

---

## 7) Creating Pandas DataFrames

### Installation

```bash
pip install pandas
```

### Creating DataFrames

**Method 1: From dictionary**
```python
import pandas as pd

# Dictionary where keys become column names
student_data = {
    'student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'math': [85, 92, 78, 88, 95],
    'science': [90, 88, 85, 92, 89],
    'english': [82, 90, 80, 85, 93],
    'class': ['A', 'A', 'B', 'A', 'B']
}

df = pd.DataFrame(student_data)
print(df)
#    student  math  science  english class
# 0    Alice    85       90       82     A
# 1      Bob    92       88       90     A
# 2  Charlie    78       85       80     B
# 3    Diana    88       92       85     A
# 4      Eve    95       89       93     B
```

**Method 2: From CSV file**
```python
import pandas as pd

df = pd.read_csv('students.csv')
print(df)
```

### DataFrame Basics

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Basic information
print(df.info())        # Data types, memory usage
print(df.describe())    # Statistics for numerical columns
print(df.head())        # First 5 rows
print(df.tail())        # Last 5 rows
print(df.columns)       # Column names
print(df.shape)         # (rows, columns)
```

### Key Points:

- DataFrames are like Excel spreadsheets
- Columns have names (unlike NumPy arrays)
- Can handle mixed data types (numbers, strings, dates)
- `pd.read_csv()` preserves structure automatically

---

## 8) Accessing DataFrame Columns

### Column Access

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Method 1: Dictionary-style (recommended)
math_scores = df['math']
print(math_scores)
# 0    85
# 1    92
# 2    78
# 3    88
# 4    95

# Method 2: Attribute-style (works, but can fail)
math_scores = df.math
print(math_scores)

# Multiple columns
subset = df[['student', 'math', 'science']]
print(subset)
```

### Working with Columns

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Calculate statistics on columns
print(f"Math average: {df['math'].mean():.2f}")
print(f"Math max: {df['math'].max()}")
print(f"Math min: {df['math'].min()}")
print(f"Math sum: {df['math'].sum()}")

# Create new column
df['total'] = df['math'] + df['science'] + df['english']
print(df)

# Access specific row
alice = df[df['student'] == 'Alice']
print(alice)
```

### Key Points:

- Use `df['column_name']` to access columns
- Prefer dictionary-style over attribute-style
- Columns support operations and statistics
- Create new columns by assignment

---

## 9) Filtering DataFrames

### Boolean Filtering

Filter rows using boolean conditions:

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Single condition
high_math = df[df['math'] > 85]
print(high_math)
# Shows only rows where math > 85

# String condition
class_a = df[df['class'] == 'A']
print(class_a)
# Shows only class A students
```

### Multiple Conditions

**Important**: Use `&` (AND) and `|` (OR), not `and`/`or`:

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Multiple conditions with &
high_math_class_a = df[(df['math'] > 85) & (df['class'] == 'A')]
print(high_math_class_a)

# Multiple conditions with |
class_a_or_b = df[(df['class'] == 'A') | (df['class'] == 'B')]
print(class_a_or_b)

# Combine filtering and column selection
names_high_math = df[df['math'] > 85]['student']
print(names_high_math)
```

### Common Filtering Patterns

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Greater than
high_scores = df[df['math'] > 90]

# Less than or equal
low_scores = df[df['math'] <= 80]

# Between values
medium_scores = df[(df['math'] >= 80) & (df['math'] <= 90)]

# Contains (for strings)
names_with_a = df[df['student'].str.contains('a', case=False)]

# Multiple column conditions
top_students = df[(df['math'] > 85) & (df['science'] > 85)]
```

### Key Points:

- Filtering uses boolean conditions: `df[condition]`
- Use `&` for AND, `|` for OR (not `and`/`or`)
- Wrap conditions in parentheses: `(condition1) & (condition2)`
- Can combine filtering with column selection

---

## 10) Reading CSV Files with Pandas

### Loading Data

```python
import pandas as pd

# Read CSV file
df = pd.read_csv('students.csv')

print(df)
print(df.head())      # First 5 rows
print(df.tail(3))     # Last 3 rows
print(df.info())      # Data types and info
```

### CSV File Format

```csv
student,math,science,english,class
Alice,85,90,82,A
Bob,92,88,90,A
Charlie,78,85,80,B
Diana,88,92,85,A
Eve,95,89,93,B
```

Pandas automatically:
- Reads headers as column names
- Infers data types
- Handles missing values
- Preserves structure

### Handling Different Formats

```python
import pandas as pd

# Different delimiter
df = pd.read_csv('data.txt', delimiter='\t')  # Tab-separated

# Skip rows
df = pd.read_csv('data.csv', skiprows=2)  # Skip first 2 rows

# Specify columns
df = pd.read_csv('data.csv', usecols=['student', 'math'])

# No header
df = pd.read_csv('data.csv', header=None, names=['col1', 'col2', 'col3'])
```

---

## 11) Basic Statistics and Calculations

### Column Statistics

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Single column statistics
print(f"Math mean: {df['math'].mean():.2f}")
print(f"Math sum: {df['math'].sum()}")
print(f"Math max: {df['math'].max()}")
print(f"Math min: {df['math'].min()}")
print(f"Math std: {df['math'].std():.2f}")

# All statistics at once
print(df['math'].describe())
# count    5.000000
# mean    87.600000
# std      6.542676
# min     78.000000
# 25%     85.000000
# 50%     88.000000
# 75%     92.000000
# max     95.000000
```

### Creating New Columns

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Simple calculation
df['total'] = df['math'] + df['science'] + df['english']

# Average score
df['average'] = df['total'] / 3

# Percentage
df['math_percent'] = (df['math'] / 100) * 100

print(df)
```

### Grouping and Aggregation

```python
import pandas as pd

df = pd.DataFrame(student_data)

# Group by class and calculate average math score
avg_by_class = df.groupby('class')['math'].mean()
print(avg_by_class)
# class
# A    88.333333
# B    86.500000

# Multiple statistics by group
stats_by_class = df.groupby('class')['math'].agg(['mean', 'max', 'min', 'sum'])
print(stats_by_class)

# Group by multiple columns
df['total'] = df['math'] + df['science'] + df['english']
avg_by_class = df.groupby('class')['total'].mean()
print(avg_by_class)
```

### Key Points:

- Use `.mean()`, `.sum()`, `.max()`, `.min()` on columns
- `.describe()` gives comprehensive statistics
- Create columns by assignment
- `groupby()` aggregates data by groups

---

## 12) When to Use What?

### NumPy vs Pandas vs Standard Python

**Use NumPy when:**
- Working with pure numerical arrays
- Need fast mathematical operations
- Performance is critical
- Data is homogeneous (all numbers)

**Use Pandas when:**
- Working with structured data (tables)
- Have column names and mixed types
- Need filtering, grouping, analysis
- Reading CSV files with headers
- Data analysis and reporting

**Use Standard Python when:**
- Small datasets (< 100 rows)
- Simple operations
- Don't need performance
- Libraries add unnecessary complexity

### Example Decision Tree:

```
Is your data a table with column names?
├─ Yes → Use Pandas
└─ No → Is it pure numbers?
    ├─ Yes → Use NumPy (if performance matters)
    └─ No → Use Standard Python lists/dicts
```

---

## 13) What We Covered

1. **The problem** - Why lists are slow for large datasets
2. **NumPy basics** - Arrays vs lists, element-wise operations
3. **Creating arrays** - `np.array()`, `np.arange()`, `np.linspace()`
4. **Array operations** - Element-wise math, statistics
5. **CSV reading** - `np.loadtxt()` for numerical data
6. **Pandas basics** - DataFrames vs arrays, structured data
7. **Creating DataFrames** - From dictionaries and CSV files
8. **Column access** - `df['column']`, statistics
9. **Filtering** - Boolean conditions, multiple filters
10. **CSV reading** - `pd.read_csv()` with headers
11. **Statistics** - Column stats, grouping, aggregation
12. **When to use what** - NumPy vs Pandas vs Python

---

## 14) Key Takeaways

1. **NumPy for numbers** - Fast arrays for numerical operations
2. **Pandas for tables** - DataFrames for structured data
3. **Element-wise operations** - Work automatically in NumPy
4. **Column access** - `df['column']` in Pandas
5. **Boolean filtering** - `df[condition]` with `&` and `|`
6. **Built-in statistics** - `.mean()`, `.sum()`, `.max()`, `.min()`
7. **Grouping** - `groupby()` for aggregations
8. **CSV reading** - `np.loadtxt()` for numbers, `pd.read_csv()` for tables
9. **Use when needed** - Not always necessary for small data
10. **Performance** - NumPy/Pandas are faster for large datasets

---

## 15) Practice Exercises

1. Create NumPy arrays and perform element-wise operations
2. Read a CSV file with NumPy and calculate statistics
3. Create a Pandas DataFrame from a dictionary
4. Filter a DataFrame with multiple conditions
5. Group data and calculate averages by category
6. Read a CSV file with Pandas and analyze it

---

## Summary

NumPy and Pandas are powerful tools for data manipulation:
- **NumPy**: Fast numerical arrays and operations
- **Pandas**: Structured data (tables) with column names
- **Use when**: Large datasets or complex analysis needed
- **Don't use when**: Small datasets or simple operations

Remember: These are tools - use them when they help, not always!

---

## 60-Second Recap

- **NumPy for numbers** - Fast arrays, element-wise operations
- **Pandas for tables** - DataFrames with column names
- **Element-wise math** - Works automatically, no loops
- **Column access** - `df['column']` gets column data
- **Boolean filtering** - `df[condition]` filters rows
- **Use `&` and `|`** - Not `and`/`or` for multiple conditions
- **Built-in stats** - `.mean()`, `.sum()`, `.max()`, `.min()`
- **Grouping** - `groupby()` aggregates by category
- **CSV reading** - `np.loadtxt()` for numbers, `pd.read_csv()` for tables
- **Use when needed** - Not always necessary for small data

---

## Mini Q&A

**Q: What's the difference between NumPy and Pandas?**  
A: NumPy is for numerical arrays (pure numbers). Pandas is for structured data (tables with column names and mixed types). Pandas uses NumPy under the hood.

**Q: When should I use NumPy vs Pandas?**  
A: NumPy for pure numerical operations. Pandas for tables with column names, mixed types, or data analysis tasks.

**Q: Do I always need NumPy/Pandas?**  
A: No! For small datasets (< 100 rows) or simple operations, standard Python is fine. Use these libraries when you need performance or complex analysis.

**Q: Why do I get errors with `&` and `|` instead of `and` and `or`?**  
A: NumPy and Pandas use `&` (AND) and `|` (OR) for element-wise operations. Python's `and`/`or` don't work with arrays/DataFrames. Always wrap conditions in parentheses: `df[(condition1) & (condition2)]`.

**Q: How do I access a column in Pandas?**  
A: Use `df['column_name']` (dictionary-style). `df.column_name` works but can fail with certain column names.

**Q: What's the difference between `df['column']` and `df.column`?**  
A: Both work, but `df['column']` is safer (works with spaces in names, reserved words). `df.column` is shorter but can fail. Prefer `df['column']`.

**Q: How do I filter rows in Pandas?**  
A: Use boolean conditions: `df[df['column'] > value]`. For multiple conditions, use `&` (AND) or `|` (OR) with parentheses.

**Q: Can I mix NumPy and Pandas?**  
A: Yes! Pandas uses NumPy arrays internally. Convert with `df['column'].values` (DataFrame to array) or `pd.DataFrame(array)` (array to DataFrame).

**Q: How do I read CSV files?**  
A: Use `np.loadtxt()` for numerical data only, or `pd.read_csv()` for tables with headers and mixed types.

**Q: What if I get "ModuleNotFoundError: No module named 'numpy'"?**  
A: Install with `pip install numpy pandas`. Add to `requirements.txt` for your project.

**Q: How do I calculate statistics?**  
A: Use `.mean()`, `.sum()`, `.max()`, `.min()` on columns, or `np.mean()`, `np.sum()` on arrays. Use `.describe()` for comprehensive stats.

**Q: How do I group data?**  
A: Use `df.groupby('column')['other_column'].mean()` to group and aggregate. Works with multiple statistics too.

**Q: What's the difference between NumPy arrays and Python lists?**  
A: Arrays print without commas `[1 2 3]`, support element-wise operations automatically, and are faster for numerical work. Lists are more flexible but slower.

**Q: How do I create a new column in Pandas?**  
A: Assign directly: `df['new_column'] = df['col1'] + df['col2']`. Pandas handles the calculation automatically.
