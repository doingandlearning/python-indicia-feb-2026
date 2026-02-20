"""
Database models (tables).

Each class represents a database table. Models inherit from Base
and define table structure using Column definitions.
"""

from database import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from datetime import datetime


class Author(Base):
    """
    Author model - represents authors table.
    
    Attributes:
        author_id: Unique identifier (primary key)
        name: Author's full name
        email: Email address (unique)
        country: Country of origin
        created_at: Timestamp when record was created
    """
    __tablename__ = "authors"
    
    author_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    country = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        """String representation of Author object."""
        return f"<Author(author_id='{self.author_id}', name='{self.name}')>"


class Book(Base):
    """
    Book model - represents books table.
    
    Attributes:
        book_id: Unique identifier (primary key)
        title: Book title
        author_id: Foreign key to authors table
        isbn: ISBN number (optional)
        published_year: Year the book was published
    """
    __tablename__ = "books"
    
    book_id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(String, ForeignKey('authors.author_id'), nullable=False)
    isbn = Column(String, unique=True)
    published_year = Column(Integer, nullable=True)
    
    def __repr__(self):
        """String representation of Book object."""
        return f"<Book(book_id='{self.book_id}', title='{self.title}')>"
