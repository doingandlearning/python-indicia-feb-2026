"""
ORM - Object Relational Mapping

- Python class -> Database table
- Class attributes -> Table columns
- Class instances -> Table rows
"""

cursor.execute("INSERT INTO authors VALUES (?, ?, ?)", (id, name, email))

author = Author(author_id=id, name=name, email=email)
session.add(author)
session.commit()

pip install sqlalchemy