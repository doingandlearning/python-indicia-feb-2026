# 08: Classes and Object-Oriented Programming

## Why this matters

Classes group related data and behavior together. Instead of managing separate variables and functions, classes create cohesive units that model real-world entities.

Good class usage gives you:
- Organized code structure
- Data and behavior together
- Reusable components
- Better code organization
- Easier maintenance

---

## 1) Core OOP Vocabulary

### Key terms
- **Class**: Blueprint/template for creating objects
- **Object/Instance**: Concrete item created from a class
- **Attribute**: Data stored in an object (like variables)
- **Method**: Function defined in a class (behavior)
- **Constructor**: Special method (`__init__`) that creates objects

### Simple analogy
- **Class** = Cookie cutter
- **Object** = Cookie made from the cutter
- **Attributes** = Properties of the cookie (size, flavor)
- **Methods** = Things the cookie can do (be eaten, crumble)

---

## 2) Creating a Simple Class

### Basic class definition
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance (object)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access attributes
print(person1.name)  # Alice
print(person1.age)   # 25
```

### Understanding `self`
```python
class Person:
    def __init__(self, name, age):
        # self refers to THIS instance
        self.name = name  # Store name on THIS object
        self.age = age    # Store age on THIS object
```

### Rule of thumb
- `self` is the first parameter of every instance method
- `self` refers to the current instance
- Use `self.attribute` to access instance attributes
- `self` is passed automatically - don't pass it when calling

---

## 3) The `__init__` Method

Constructor method - runs when object is created:

```python
class Employee:
    def __init__(self, name, employee_id, department, salary):
        # Initialize attributes
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

# Create object - __init__ runs automatically
emp = Employee("Alice", "E001", "Engineering", 75000)
```

### Default values
```python
class Employee:
    def __init__(self, name, employee_id, department="General", salary=50000):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

# Use defaults
emp1 = Employee("Alice", "E001")  # Uses defaults for department and salary
emp2 = Employee("Bob", "E002", "Sales", 60000)  # Override defaults
```

### Rule of thumb
- `__init__` initializes object attributes
- Always include `self` as first parameter
- Set all important attributes in `__init__`

---

## 4) Instance Methods

Methods define what objects can do:

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account."""
        self.balance += amount
    
    def withdraw(self, amount):
        """Remove money from account."""
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        """Return current balance."""
        return self.balance

# Use methods
account = BankAccount("ACC001", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 1300
```

### Rule of thumb
- Methods are functions inside classes
- First parameter is always `self`
- Methods can access `self.attribute` to read/modify data
- Call methods on instances: `object.method()`

---

## 5) The `__str__` Method

Controls how object is printed:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 25)
print(person)  # Person(name='Alice', age=25)
```

### Without `__str__`
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person)  # <__main__.Person object at 0x...> (not helpful!)
```

### Rule of thumb
- Always implement `__str__` for debugging
- `__str__` should return a readable string representation
- Makes objects much easier to work with

---

## 6) Comparison Methods

Make objects comparable:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __eq__(self, other):
        """Equal if same salary."""
        return self.salary == other.salary
    
    def __lt__(self, other):
        """Less than if lower salary."""
        return self.salary < other.salary
    
    def __le__(self, other):
        """Less than or equal."""
        return self.salary <= other.salary

emp1 = Employee("Alice", 75000)
emp2 = Employee("Bob", 80000)

print(emp1 < emp2)  # True (75000 < 80000)
print(emp1 == emp2)  # False
```

### Common comparison methods
- `__eq__` - `==` (equal)
- `__ne__` - `!=` (not equal)
- `__lt__` - `<` (less than)
- `__le__` - `<=` (less than or equal)
- `__gt__` - `>` (greater than)
- `__ge__` - `>=` (greater than or equal)

---

## 7) Why Classes Over Raw Dictionaries?

### Dictionary approach
```python
# Using dictionaries
person1 = {"name": "Alice", "age": 25}
person2 = {"name": "Bob", "age": 30}

# Problems:
# - No type safety
# - Easy to make typos in keys
# - No methods/behavior
# - Hard to ensure consistency
```

### Class approach
```python
# Using classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def is_adult(self):
        return self.age >= 18

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Benefits:
# - Type safety
# - IDE autocomplete
# - Methods encapsulate behavior
# - Consistent structure
```

### Rule of thumb
- Use dictionaries for simple, transient data
- Use classes for rich domain models with behavior
- Classes improve readability, consistency, and maintainability

---

## 8) Class Attributes vs Instance Attributes

### Instance attributes (per object)
```python
class Person:
    def __init__(self, name):
        self.name = name  # Instance attribute

person1 = Person("Alice")
person2 = Person("Bob")
print(person1.name)  # Alice
print(person2.name)  # Bob (different value)
```

### Class attributes (shared)
```python
class Person:
    species = "Homo sapiens"  # Class attribute (shared)
    
    def __init__(self, name):
        self.name = name  # Instance attribute

person1 = Person("Alice")
person2 = Person("Bob")

print(person1.species)  # Homo sapiens
print(person2.species)  # Homo sapiens (same value)
print(Person.species)   # Homo sapiens (accessed via class)
```

### Rule of thumb
- Instance attributes: `self.attribute` - unique per object
- Class attributes: `Class.attribute` - shared by all instances
- Use class attributes for constants or shared data

---

## 9) Common Patterns

### Data class pattern
```python
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"{self.name} (${self.price})"
    
    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)
```

### Validation pattern
```python
class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age
```

### Method chaining pattern
```python
class StringBuilder:
    def __init__(self):
        self.parts = []
    
    def add(self, text):
        self.parts.append(text)
        return self  # Return self for chaining
    
    def build(self):
        return "".join(self.parts)

# Chain methods
result = StringBuilder().add("Hello").add(" ").add("World").build()
```

---

## Common Mistakes + Fixes

- **Mistake**: Missing `self` in method definitions  
  **Fix**: Instance methods always include `self` first: `def method(self, ...):`

- **Mistake**: Accessing attributes before assignment  
  **Fix**: Initialize in `__init__` before using

- **Mistake**: Forgetting `self.` when accessing attributes  
  **Fix**: Use `self.attribute` not just `attribute`

- **Mistake**: Calling methods without creating instance  
  **Fix**: Create object first: `obj = Class()` then `obj.method()`

- **Mistake**: Not implementing `__str__`  
  **Fix**: Always add `__str__` for readable output

- **Mistake**: Modifying class attributes via instance  
  **Fix**: Use `Class.attribute` for class attributes, or be aware it creates instance attribute

---

## Best Practices

1. **Keep classes focused**
   ```python
   # Good - single responsibility
   class BankAccount:
       def __init__(self, balance):
           self.balance = balance
       def deposit(self, amount):
           ...
   
   # Avoid - does too much
   class BankAccount:
       # Handles account, transactions, reporting, email...
   ```

2. **Use meaningful names**
   ```python
   # Good
   class CustomerAccount:
       ...
   
   # Avoid
   class CA:
       ...
   ```

3. **Initialize all attributes in `__init__`**
   ```python
   # Good
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age
   
   # Avoid
   class Person:
       def __init__(self, name):
           self.name = name
           # age set later - confusing!
   ```

4. **Always implement `__str__`**
   ```python
   class Person:
       def __str__(self):
           return f"Person(name='{self.name}')"
   ```

5. **Keep methods focused**
   ```python
   # Good - single responsibility
   def calculate_total(self):
       return self.price * self.quantity
   
   # Avoid - does multiple things
   def process_order(self):
       # Calculates total, applies discount, sends email, updates database...
   ```

---

## Quick Lab Checklist

Before submission, verify:

- [ ] I can define and instantiate a class
- [ ] I can store data on `self` (instance attributes)
- [ ] I can add useful class methods
- [ ] I can implement `__init__` correctly
- [ ] I can implement `__str__` for readable output
- [ ] I understand the difference between class and instance attributes
- [ ] I can use methods to encapsulate behavior

---

## 60-Second Recap

- **Classes model real entities** - Group related data and behavior
- **Objects hold state + behavior** - Attributes store data, methods define actions
- **`__init__` initializes objects** - Sets up attributes when object is created
- **`__str__` makes objects printable** - Returns readable string representation
- **`self` refers to the instance** - Always first parameter of instance methods
- **Classes improve organization** - Better than dictionaries for rich models

---

## Mini Q&A

**Q: Should everything be a class?**  
A: No - use classes when data + behavior naturally belong together. Simple data can use dictionaries.

**Q: Dict or class?**  
A: Dict for simple transient data. Class for rich domain models with behavior.

**Q: What is `self`?**  
A: `self` refers to the current instance. It's automatically passed when calling methods.

**Q: Do I always need `__init__`?**  
A: No, but it's very common. Use it to initialize attributes when object is created.

**Q: Can I have methods without `self`?**  
A: Yes - use `@staticmethod` decorator, but instance methods (with `self`) are more common.

**Q: What's the difference between class and instance attributes?**  
A: Class attributes are shared by all instances. Instance attributes are unique to each object.

**Q: How do I make objects comparable?**  
A: Implement comparison methods like `__eq__`, `__lt__`, etc.

**Q: Can I modify attributes directly?**  
A: Yes, but consider using methods for validation or encapsulation: `person.age = 25` vs `person.set_age(25)`.
