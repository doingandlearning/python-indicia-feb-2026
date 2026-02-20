from setup import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime


class Author(Base):
  __tablename__ = "authors"  # let's me control what the table is called

  author_id = Column(String, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=True, unique=True)
  country = Column(String)
  created_at = Column(DateTime, default=datetime.now)