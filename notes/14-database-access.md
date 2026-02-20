# 14: Database Access with SQLAlchemy ORM

## Why this matters

Most applications need to store and retrieve data persistently. Databases are the standard way to do this, but writing raw SQL can be error-prone and database-specific.

SQLAlchemy ORM (Object-Relational Mapping) lets you:
- Work with databases using Python classes instead of SQL
- Write database-agnostic code (works with SQLite, PostgreSQL, MySQL, etc.)
- Avoid SQL injection vulnerabilities automatically
- Get IDE autocomplete and type checking
- Focus on business logic, not database details

---

## 1) What is ORM?

### Object-Relational Mapping Explained

**ORM** maps Python objects to database tables:
- Python class = Database table
- Class attributes = Table columns
- Class instances = Table rows

### Why use ORM instead of raw SQL?

**Raw SQL approach:**
```python
cursor.execute("INSERT INTO authors VALUES (?, ?, ?)", (id, name, email))
```

**ORM approach:**
```python
author = Author(author_id=id, name=name, email=email)
session.add(author)
session.commit()
```

**Benefits:**
- ✅ Python code instead of SQL strings
- ✅ Type safety and IDE autocomplete
- ✅ No SQL injection risk
- ✅ Works with different databases
- ✅ Automatic table creation

---

## 2) Setting Up SQLAlchemy

### Installation
```bash
pip install sqlalchemy
```

### Basic Setup
```python
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Base class for all models
Base = declarative_base()

# Create database engine (SQLite file-based database)
engine = create_engine('sqlite:///library.db', echo=False)

# Session factory - creates sessions for database operations
Session = sessionmaker(bind=engine)
```

### Key Components:
- **`Base`**: Base class that all models inherit from
- **`engine`**: Database connection (SQLite file in this case)
- **`Session`**: Factory for creating database sessions
- **`echo=False`**: Set to `True` to see SQL queries (useful for debugging)

---

## 3) Defining Models (Database Tables)

### Creating Your First Model

Models are Python classes that represent database tables:

```python
class Author(Base):
    """Author model - represents authors table."""
    __tablename__ = 'authors'
    
    author_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    country = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Author(author_id='{self.author_id}', name='{self.name}')>"
```

### Understanding Model Components:

**`__tablename__`**: Name of the database table
- Must be unique
- Convention: lowercase, plural (e.g., `authors`, `books`)

**`Column()`**: Defines a table column
- First argument: data type (`String`, `Integer`, `Float`, `DateTime`, etc.)
- `primary_key=True`: Unique identifier for each row
- `nullable=False`: Field is required (cannot be None)
- `unique=True`: No duplicate values allowed
- `default=...`: Default value if not provided

**Common Column Types:**
- `String`: Text data
- `Integer`: Whole numbers
- `Float`: Decimal numbers
- `DateTime`: Date and time
- `Boolean`: True/False

### Creating Tables from Models

```python
# Create all tables defined by models
Base.metadata.create_all(engine)
```

This creates the database tables automatically based on your model definitions. If tables already exist, it won't recreate them.

---

## 4) Sessions: Managing Database Connections

### What is a Session?

A **session** manages a connection to the database:
- Tracks changes to objects
- Handles transactions (commit/rollback)
- Provides query interface
- Must be closed when done

### Session Lifecycle Pattern

```python
def add_author(author_id, name, email, country=None):
    session = Session()  # Create session
    try:
        # Do database operations
        author = Author(author_id=author_id, name=name, email=email, country=country)
        session.add(author)
        session.commit()  # Save changes
        return True
    except Exception as e:
        session.rollback()  # Undo changes on error
        print(f"Error: {e}")
        return False
    finally:
        session.close()  # Always close session
```

### Key Session Methods:

- **`session.add(object)`**: Add object to session (staged for insert)
- **`session.commit()`**: Save all changes to database
- **`session.rollback()`**: Undo changes since last commit
- **`session.close()`**: Close the session (always do this!)

### Why `try/except/finally`?

- **`try`**: Attempt database operations
- **`except`**: Handle errors gracefully
- **`finally`**: Always close session, even if error occurs

---

## 5) Creating Records (INSERT)

### Adding Data to Database

```python
from sqlalchemy.exc import IntegrityError

def add_author(author_id, name, email, country=None):
    session = Session()
    try:
        # Create model instance (like any Python object)
        author = Author(
            author_id=author_id,
            name=name,
            email=email,
            country=country
        )
        
        # Add to session
        session.add(author)
        
        # Commit to save
        session.commit()
        print(f"Author {author_id} added successfully")
        return True
    except IntegrityError as e:
        # Handle duplicate key/email errors
        session.rollback()
        print(f"Error: Author already exists")
        return False
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
        return False
    finally:
        session.close()

# Usage
add_author("AUTH001", "Jane Austen", "jane@email.com", "United Kingdom")
```

### Key Points:

- Create model instances like regular Python objects
- `session.add()` stages the object for insertion
- `session.commit()` actually saves to database
- Handle `IntegrityError` for duplicate keys/emails
- Always close session in `finally` block

---

## 6) Reading Records (SELECT)

### Querying the Database

SQLAlchemy provides a Python-like query interface:

```python
def get_author(author_id):
    """Get a single author by ID."""
    session = Session()
    try:
        author = session.query(Author).filter(
            Author.author_id == author_id
        ).first()
        return author  # Returns Author object or None
    except Exception as e:
        print(f"Database error: {e}")
        return None
    finally:
        session.close()

def get_all_authors():
    """Get all authors."""
    session = Session()
    try:
        authors = session.query(Author).order_by(Author.name).all()
        return authors  # Returns list of Author objects
    except Exception as e:
        print(f"Database error: {e}")
        return []
    finally:
        session.close()

def search_authors_by_name(search_term):
    """Search authors by name."""
    session = Session()
    try:
        authors = session.query(Author).filter(
            Author.name.like(f"%{search_term}%")
        ).order_by(Author.name).all()
        return authors
    except Exception as e:
        print(f"Database error: {e}")
        return []
    finally:
        session.close()
```

### Query Methods:

- **`session.query(Model)`**: Start a query for a model
- **`.filter(condition)`**: Add WHERE clause
- **`.first()`**: Get first result (or None)
- **`.all()`**: Get all results (returns list)
- **`.order_by(field)`**: Sort results
- **`.like(pattern)`**: Pattern matching (use `%` for wildcards)

### Accessing Data:

```python
author = get_author("AUTH001")
if author:
    print(author.name)      # Access attributes directly
    print(author.email)
    print(author.country)
```

---

## 7) Updating Records (UPDATE)

### Modifying Existing Data

```python
def update_author(author_id, name=None, email=None, country=None):
    """Update author information."""
    session = Session()
    try:
        # Get existing author
        author = session.query(Author).filter(
            Author.author_id == author_id
        ).first()
        
        if not author:
            print(f"Author {author_id} not found")
            return False
        
        # Update only provided fields
        if name:
            author.name = name
        if email:
            author.email = email
        if country:
            author.country = country
        
        # Commit changes
        session.commit()
        print(f"Author {author_id} updated successfully")
        return True
    except IntegrityError as e:
        session.rollback()
        print(f"Error: {e}")
        return False
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
        return False
    finally:
        session.close()

# Usage
update_author("AUTH001", country="England")
update_author("AUTH002", name="Charles Dickens")
```

### Key Points:

- Query for object first
- Modify attributes directly (like any Python object)
- Only update fields that are provided (check for `None`)
- `session.commit()` saves changes
- Session tracks changes automatically

---

## 8) Deleting Records (DELETE)

### Removing Data

```python
def delete_author(author_id):
    """Delete an author."""
    session = Session()
    try:
        # Get author to delete
        author = session.query(Author).filter(
            Author.author_id == author_id
        ).first()
        
        if not author:
            print(f"Author {author_id} not found")
            return False
        
        # Delete the object
        session.delete(author)
        
        # Commit deletion
        session.commit()
        print(f"Author {author_id} deleted successfully")
        return True
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
        return False
    finally:
        session.close()

# Usage
delete_author("AUTH002")
```

### Key Points:

- Query for object first
- Use `session.delete(object)` to delete
- Check if object exists before deleting
- `session.commit()` saves deletion
- Always handle errors gracefully

---

## 9) Working with Relationships (Foreign Keys)

### Linking Tables Together

When one table references another, use a **foreign key**:

```python
from sqlalchemy import ForeignKey, Integer

class Book(Base):
    """Book model - linked to Author."""
    __tablename__ = 'books'
    
    book_id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(String, ForeignKey('authors.author_id'), nullable=False)
    isbn = Column(String, unique=True)
    published_year = Column(Integer)
```

### Understanding Foreign Keys:

- **`ForeignKey('authors.author_id')`**: Links to `author_id` in `authors` table
- **`nullable=False`**: Book must have an author
- Database enforces relationship (can't create book for non-existent author)

### Creating Related Records:

```python
def add_book(book_id, title, author_id, isbn=None, published_year=None):
    """Add a book by an author."""
    session = Session()
    try:
        book = Book(
            book_id=book_id,
            title=title,
            author_id=author_id,  # Reference to author
            isbn=isbn,
            published_year=published_year
        )
        session.add(book)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
        return False
    finally:
        session.close()

# Usage
add_book("BOOK001", "Pride and Prejudice", "AUTH001", "9780141439518", 1813)
```

### Querying Related Data:

```python
def get_author_books(author_id):
    """Get all books by an author."""
    session = Session()
    try:
        books = session.query(Book).filter(
            Book.author_id == author_id
        ).all()
        return books
    except Exception as e:
        print(f"Database error: {e}")
        return []
    finally:
        session.close()

def get_book(book_id):
    """Get a book by ID."""
    session = Session()
    try:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        return book
    except Exception as e:
        print(f"Database error: {e}")
        return None
    finally:
        session.close()

def get_book_with_author(book_id):
    """Get book with author information."""
    book = get_book(book_id)
    if not book:
        return None
    
    # Get author using foreign key
    author = get_author(book.author_id)
    if author:
        print(f"Book: {book.title}")
        print(f"  Author: {author.name} ({author.country})")
        print(f"  Published: {book.published_year}")
        print(f"  ISBN: {book.isbn}")
```

### Key Points:

- Foreign keys link tables together
- Use `ForeignKey()` to define relationship
- Access related data by querying with foreign key value
- Database ensures referential integrity

---

## 10) Error Handling

### Common Database Errors

**IntegrityError**: Violates constraints (duplicate key, unique violation)
```python
from sqlalchemy.exc import IntegrityError

try:
    session.add(author)
    session.commit()
except IntegrityError as e:
    session.rollback()
    print("Author already exists or email is duplicate")
```

**General Exceptions**: Other database errors
```python
try:
    # Database operations
except Exception as e:
    session.rollback()
    print(f"Database error: {e}")
```

### Best Practices:

- Always use `try/except/finally`
- Rollback on errors (`session.rollback()`)
- Close session in `finally` block
- Provide helpful error messages
- Return `True`/`False` or `None` to indicate success/failure

---

## 11) Complete CRUD Pattern

### Full Example: Customer Management

```python
def main():
    """Complete example demonstrating CRUD operations."""
    print("Library Database System")
    print("=" * 60)
    
    # CREATE - Add authors
    print("\n1. Adding authors...")
    add_author("AUTH001", "Jane Austen", "jane@email.com", "United Kingdom")
    add_author("AUTH002", "Charles Dickens", "charles@email.com", "United Kingdom")
    
    # READ - Query authors
    print("\n2. All authors:")
    authors = get_all_authors()
    for author in authors:
        print(f"  {author.author_id}: {author.name} - {author.country}")
    
    # UPDATE - Modify author
    print("\n3. Updating author...")
    update_author("AUTH001", country="England")
    
    # CREATE - Add books
    print("\n4. Adding books...")
    add_book("BOOK001", "Pride and Prejudice", "AUTH001", "9780141439518", 1813)
    add_book("BOOK002", "Sense and Sensibility", "AUTH001", "9780141439662", 1811)
    add_book("BOOK003", "Great Expectations", "AUTH002", "9780141439563", 1861)
    
    # READ - Query books
    print("\n5. Books by AUTH001:")
    books = get_author_books("AUTH001")
    for book in books:
        print(f"  {book.title} ({book.published_year})")
    
    # DELETE - Remove author (optional)
    # delete_author("AUTH002")

if __name__ == "__main__":
    main()
```

### CRUD Operations Summary:

- **Create**: `session.add()` + `session.commit()`
- **Read**: `session.query().filter().first()` or `.all()`
- **Update**: Modify attributes + `session.commit()`
- **Delete**: `session.delete()` + `session.commit()`

---

## 12) SQLite Database Files

### Understanding SQLite

- **File-based database**: Stored as `.db` file on disk
- **No server needed**: Perfect for learning and small applications
- **Persistent**: Data survives program restarts
- **Portable**: Copy `.db` file to move database

### Database File Location:

```python
engine = create_engine('sqlite:///library.db')  # Current directory
engine = create_engine('sqlite:///data/library.db')  # In data/ folder
engine = create_engine('sqlite:////absolute/path/library.db')  # Absolute path
```

### Managing Database Files:

- Database file created automatically on first run
- Delete `.db` file to start fresh
- File persists between program runs
- Can inspect with SQLite tools (optional)

---

## 13) Common Patterns and Best Practices

### Session Management Pattern

**Always use this pattern:**
```python
def database_operation():
    session = Session()
    try:
        # Do work
        session.commit()
        return result
    except Exception as e:
        session.rollback()
        handle_error(e)
        return None
    finally:
        session.close()
```

### Query Pattern

**Query, filter, get results:**
```python
# Single result
result = session.query(Model).filter(condition).first()

# Multiple results
results = session.query(Model).filter(condition).all()

# Ordered results
results = session.query(Model).order_by(Model.field).all()
```

### Update Pattern

**Get, modify, commit:**
```python
object = session.query(Model).filter(condition).first()
if object:
    object.field = new_value
    session.commit()
```

### Delete Pattern

**Get, delete, commit:**
```python
object = session.query(Model).filter(condition).first()
if object:
    session.delete(object)
    session.commit()
```

---

## 14) What We Covered

1. **ORM basics** - Python classes represent database tables
2. **Model definition** - Using `Base`, `Column()`, and field types
3. **Sessions** - Managing database connections and transactions
4. **Creating records** - `session.add()` and `session.commit()`
5. **Reading records** - `session.query()` with filters
6. **Updating records** - Modify attributes and commit
7. **Deleting records** - `session.delete()` and commit
8. **Foreign keys** - Linking tables together (books reference authors)
9. **Error handling** - `IntegrityError` and general exceptions
10. **SQLite** - File-based database storage

---

## 15) Key Takeaways

1. **ORM uses Python classes** - Models represent database tables
2. **Sessions manage connections** - Create, use, close sessions
3. **CRUD operations** - Create (add), Read (query), Update, Delete
4. **Foreign keys link tables** - Books reference authors
5. **Query API is Python** - No SQL strings needed
6. **Always handle errors** - Use try/except/finally
7. **Commit changes** - `session.commit()` saves data
8. **SQLite is file-based** - Database stored in `.db` file
9. **Close sessions** - Always in `finally` block
10. **Type safety** - IDE autocomplete and type checking

---

## 16) Practice Exercises

1. Create a `Product` model with fields: `product_id`, `name`, `price`, `stock`
2. Write functions to add, get, update, and delete products
3. Add a `Category` model and link products to categories
4. Write a function to get all products in a category
5. Add validation to prevent negative stock values

---

## Summary

SQLAlchemy ORM lets you work with databases using Python classes instead of SQL. Key concepts:
- **Models**: Python classes that represent tables
- **Sessions**: Manage database connections and transactions
- **CRUD**: Create, Read, Update, Delete operations
- **Foreign Keys**: Link tables together
- **Error Handling**: Always use try/except/finally

Remember: ORM makes database work feel like regular Python programming!

---

## 60-Second Recap

- **ORM maps Python to databases** - Classes = tables, instances = rows
- **SQLAlchemy is the standard** - Most popular Python ORM
- **Models inherit from Base** - Defines database tables
- **Sessions manage connections** - Create, commit, close
- **CRUD operations** - Add, query, modify, delete
- **Foreign keys link tables** - Books reference authors
- **Query API is Python** - No SQL strings needed
- **Always handle errors** - Use try/except/finally
- **Commit saves changes** - `session.commit()` writes to database
- **SQLite is file-based** - Perfect for learning

---

## Mini Q&A

**Q: What is ORM?**  
A: Object-Relational Mapping - maps Python classes to database tables. Lets you work with databases using Python instead of SQL.

**Q: Why use ORM instead of raw SQL?**  
A: Type safety, IDE autocomplete, no SQL injection risk, database-agnostic code, and automatic table creation.

**Q: What is a session?**  
A: A session manages a database connection. It tracks changes, handles transactions, and provides the query interface.

**Q: When do I need to commit?**  
A: After making changes (add, update, delete). `session.commit()` saves changes to the database.

**Q: What happens if I don't close a session?**  
A: Database connections remain open, which can cause resource leaks. Always close in `finally` block.

**Q: How do I query for a single record?**  
A: Use `.first()` - returns the first match or `None` if not found.

**Q: How do I query for multiple records?**  
A: Use `.all()` - returns a list of all matching records.

**Q: What is a foreign key?**  
A: A field that references another table's primary key. Links tables together (e.g., book.author_id → author.author_id).

**Q: Can I use ORM with different databases?**  
A: Yes! SQLAlchemy works with SQLite, PostgreSQL, MySQL, and others. Just change the connection string.

**Q: What is SQLite?**  
A: A file-based database. Perfect for learning - no server needed, data stored in a `.db` file.

**Q: How do I handle duplicate key errors?**  
A: Catch `IntegrityError` from `sqlalchemy.exc` and handle gracefully with a rollback.

**Q: Do I need to write SQL?**  
A: No! ORM handles SQL generation automatically. You write Python code, SQLAlchemy writes SQL.

**Q: How do I update only some fields?**  
A: Check if field is provided (not `None`), then update only those fields before committing.

**Q: What's the difference between `add()` and `commit()`?**  
A: `add()` stages the object for insertion. `commit()` actually saves it to the database.
