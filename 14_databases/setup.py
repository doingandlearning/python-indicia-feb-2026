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

# CRUD -> Create, Read, Update, Delete
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