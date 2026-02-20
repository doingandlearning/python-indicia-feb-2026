"""
Database configuration and setup.

This module contains the database engine, session factory, and base class
for all models. This is the only place that needs to change if you switch
database types (SQLite, PostgreSQL, MySQL, etc.).
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for all models
Base = declarative_base()

# Database engine - only line that changes if you change database type
# Set echo=True to see SQL queries (useful for debugging)
engine = create_engine('sqlite:///library.db', echo=False)

# Session factory - creates sessions for database operations
Session = sessionmaker(bind=engine)


def create_tables():
    """Create all database tables from model definitions."""
    Base.metadata.create_all(engine)
    print("Database tables created successfully")


def get_session():
    """
    Get a new database session.
    
    Returns:
        Session: A new database session
    """
    return Session()
