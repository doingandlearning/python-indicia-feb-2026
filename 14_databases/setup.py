from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

# engine - the only line that changes if you change db type
# set echo to True if you want to debug the SQL queries
engine = create_engine('sqlite:///library.db', echo=False)


Session = sessionmaker(bind=engine)