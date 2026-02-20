from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

# engine - the only line that changes if you change db type
# set echo to True if you want to debug the SQL queries
engine = create_engine('sqlite:///library.db', echo=False)

Session = sessionmaker(bind=engine)

class Author(Base):
  __tablename__ = "authors"  # let's me control what the table is called

  author_id = Column(String, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=True, unique=True)
  country = Column(String)
  created_at = Column(DateTime, default=datetime.now)

  def __repr__(self):
    return f"<Author(author_id='{self.author_id}', name='{self.name}')>"

Base.metadata.create_all(engine)

# CRUD -> Create (INSERT), Read (SELECT), Update, Delete
def add_author(author_id, name, email, country=None):
  session = Session()
  try:
    author = Author(author_id=author_id, name=name, email=email, country=country)
    session.add(author)
    session.commit()
    return True
  except Exception as e:
    session.rollback()
    print(f"Error {e}")
    return False
  finally:
    session.close()

# add_author("1", "Robert Jordan", "robert@jordan.com", "USA")

def get_author_by_id(author_id):
  session = Session()
  try:
    author = session.query(Author).filter(Author.author_id == author_id).first()
    return author
  finally:
    session.close()

my_author = get_author_by_id("1")
print(my_author)
print(type(my_author))

def get_all_authors():
    """Get all authors."""
    session = Session()
    try:  # SELECT * FROM authors ORDER BY name;
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
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
        return False
    finally:
        session.close()

# update_author("1", country="UK")

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