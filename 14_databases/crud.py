"""
CRUD operations for database models.

CRUD = Create, Read, Update, Delete
These functions provide a clean interface for database operations.
"""

from sqlalchemy.exc import IntegrityError
from database import Session
from models import Author


# CREATE operations
def add_author(author_id, name, email, country=None):
    """
    Add a new author to the database.
    
    Args:
        author_id: Unique identifier for the author
        name: Author's full name
        email: Email address (must be unique)
        country: Country of origin (optional)
    
    Returns:
        bool: True if successful, False otherwise
    """
    session = Session()
    try:
        author = Author(
            author_id=author_id,
            name=name,
            email=email,
            country=country
        )
        session.add(author)
        session.commit()
        print(f"Author {author_id} added successfully")
        return True
    except IntegrityError as e:
        session.rollback()
        print(f"Error: Author with ID {author_id} or email {email} already exists")
        return False
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
        return False
    finally:
        session.close()


# READ operations
def get_author_by_id(author_id):
    """
    Get an author by their ID.
    
    Args:
        author_id: Unique identifier for the author
    
    Returns:
        Author: Author object if found, None otherwise
    """
    session = Session()
    try:
        author = session.query(Author).filter(
            Author.author_id == author_id
        ).first()
        return author
    except Exception as e:
        print(f"Database error: {e}")
        return None
    finally:
        session.close()


def get_all_authors():
    """
    Get all authors, ordered by name.
    
    Returns:
        list: List of Author objects
    """
    session = Session()
    try:
        authors = session.query(Author).order_by(Author.name).all()
        return authors
    except Exception as e:
        print(f"Database error: {e}")
        return []
    finally:
        session.close()


def search_authors_by_name(search_term):
    """
    Search authors by name (case-insensitive partial match).
    
    Args:
        search_term: Text to search for in author names
    
    Returns:
        list: List of matching Author objects
    """
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


# UPDATE operations
def update_author(author_id, name=None, email=None, country=None):
    """
    Update author information.
    
    Args:
        author_id: Unique identifier for the author
        name: New name (optional)
        email: New email (optional)
        country: New country (optional)
    
    Returns:
        bool: True if successful, False otherwise
    """
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


# DELETE operations
def delete_author(author_id):
    """
    Delete an author from the database.
    
    Args:
        author_id: Unique identifier for the author
    
    Returns:
        bool: True if successful, False otherwise
    """
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
