# Import the FastAPI class. This is essential for creating a FastAPI application.
from fastapi import FastAPI

# Import the 'models' module. 
# This typically contains the SQLAlchemy ORM models that define the structure of your database tables.
import models

# Import 'engine' from the 'database' module.
# 'engine' is the SQLAlchemy engine instance that you've configured for database interaction.
from database import engine

# Create an instance of the FastAPI class.
# This instance, 'app', is the main point of your web application, handling all the requests.
app = FastAPI()

# Create the database tables based on the models defined in the 'models' module.
# This line checks your models and creates tables for them in the database if they don't already exist.
# The 'bind=engine' argument tells SQLAlchemy which database engine to use for this operation.
models.Base.metadata.create_all(bind=engine)
