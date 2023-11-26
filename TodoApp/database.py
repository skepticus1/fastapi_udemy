# Import necessary components from SQLAlchemy.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database URL. 
# In this case, it's a SQLite database named 'todos.db' located in the current directory.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

# Create an SQLAlchemy engine.
# This engine manages the connection to the database.
# For SQLite, 'check_same_thread' is set to False to allow the use of the same database connection in different threads.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create a session factory using the engine.
# 'SessionLocal' is a factory that will produce new session objects when called.
# These sessions are used to talk to the database. 'autocommit' is False, meaning changes are not automatically committed.
# 'autoflush' is False, meaning the session will not automatically flush changes to the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative classes.
# This base class will allow the definition of SQLAlchemy ORM models. Models will inherit from this class.
Base = declarative_base()
