# Import the 'Base' class from the database module, which was defined in your database.py.
# This base class is used to define ORM models in SQLAlchemy.
from database import Base

# Import necessary column types from SQLAlchemy.
from sqlalchemy import Column, Integer, String, Boolean

# Define a class 'Todos', which represents a table in the database.
# This class inherits from 'Base', linking it to SQLAlchemy's ORM system.
class Todos(Base):
    # Define the name of the table in the database.
    __tablename__ = 'todos'

    # Define columns in the table.
    # Each attribute of the class corresponds to a column in the database table.
    
    # 'id' is an integer column, set as the primary key. 
    # 'index=True' makes searches based on this column faster.
    id = Column(Integer, primary_key=True, index=True)

    # 'title' is a string column to store the title of a todo item.
    title = Column(String)

    # 'description' is a string column to store the description of the todo item.
    description = Column(String)

    # 'priority' is an integer column to store the priority of the todo item.
    priority = Column(Integer)

    # 'complete' is a boolean column to store whether the todo item is complete.
    # It has a default value of False, meaning new records will be marked as incomplete by default.
    complete = Column(Boolean, default=False)
