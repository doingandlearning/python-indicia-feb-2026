# Database Example - Best Practices Structure

This directory demonstrates best practices for organizing SQLAlchemy database code.

## File Structure

```
14_databases/
├── database.py      # Database configuration (engine, session, Base)
├── models.py        # Database models (tables)
├── crud.py          # CRUD operations (Create, Read, Update, Delete)
├── example.py       # Example usage/demo
└── README.md        # This file
```

## Best Practices Demonstrated

### 1. **Separation of Concerns**
- **`database.py`**: Only database configuration
- **`models.py`**: Only model definitions
- **`crud.py`**: Only database operations
- **`example.py`**: Only usage examples

### 2. **Avoid Circular Imports**
- Models import from `database.py` (one-way dependency)
- CRUD functions import from `models.py` and `database.py`
- Example imports from all modules
- No circular dependencies!

### 3. **Proper Error Handling**
- Use `IntegrityError` for duplicate key/unique violations
- Always use `try/except/finally` for sessions
- Always close sessions in `finally` block
- Rollback on errors

### 4. **Clear Documentation**
- Docstrings for all functions
- Comments explaining important concepts
- Type hints in docstrings

### 5. **Session Management**
- Create session at start of function
- Close session in `finally` block
- Rollback on errors
- Commit only on success

## Usage

### Setup

1. Install dependencies:
```bash
pip install sqlalchemy
```

2. Run the example:
```bash
python example.py
```

### Creating Your Own Models

1. Add model to `models.py`:
```python
class YourModel(Base):
    __tablename__ = "your_table"
    # ... columns ...
```

2. Add CRUD functions to `crud.py`:
```python
def add_your_model(...):
    # ... implementation ...
```

3. Import and use in your code:
```python
from crud import add_your_model
add_your_model(...)
```

## Key Concepts

- **Base**: Base class all models inherit from
- **Session**: Manages database connection and transactions
- **Models**: Python classes representing database tables
- **CRUD**: Create, Read, Update, Delete operations

## Import Pattern

```
database.py  (defines Base, engine, Session)
    ↑
    |
models.py  (imports Base, defines models)
    ↑
    |
crud.py  (imports models and database, defines operations)
    ↑
    |
example.py  (imports everything, demonstrates usage)
```

This structure ensures:
- ✅ No circular imports
- ✅ Clear separation of concerns
- ✅ Easy to maintain and extend
- ✅ Follows Python best practices
