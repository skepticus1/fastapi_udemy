from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

# Initialize FastAPI app. What the variable is called (here app) will be what is used in the cmd.
app = FastAPI()

# Define a basic Book class to represent books in the application
class Book:
    # Define the class attributes with type annotations
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    # Constructor method to initialize a Book object with provided values
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id  # Set the book id
        self.title = title  # Set the book title
        self.author = author  # Set the author's name
        self.description = description  # Set the book description
        self.rating = rating  # Set the book rating
        self.published_date = published_date


# Define a Pydantic model for book data validation
class BookRequest(BaseModel):
    id: Optional[int] = None  # Optional ID field, default to None
    title: str = Field(min_length=3)  # Title must be at least 3 characters
    author: str = Field(min_length=1)  # Author must be at least 1 character
    description: str = Field(min_length=1, max_length=100)  # Description length restrictions
    rating: int = Field(gt=0, lt=6)  # Rating must be between 0 and 5
    published_date: int = Field(gt=0, lt=2023)

    # Configuration class to specify additional settings
    class Config:
        # Provide example data for Swagger UI documentation
        json_schema_extra = {
            'example':{
                'title':'A new book',
                'author':'A new Author',
                'description':'A description of a new book',
                'rating':5,
                'published_date': 2000,
            }
        }


# A pre-filled list of books to simulate a database
BOOKS = [
    Book(1, "CompSci", "CodingCo", "Good Book", 5, 2),
    Book(2, "CompSci2", "CodingCo2", "Good Book2", 5, 2),
    Book(3, "CompSci3", "CodingCo3", "Bad Book", 5, 3),
    Book(4, "CompSci4", "CodingCo4", "Book Book", 5, 4),
    Book(5, "CompSci5", "CodingCo5", "Good Door", 5, 5),
]

# Endpoint to get a list of all books
@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    # If the BOOKS list is empty, return a message indicating no books are available
    if len(BOOKS) == 0:
        return "You have no books"
    # Otherwise, return the list of books
    return BOOKS

# Endpoint to get a book by id using path param
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)): # Path is a validation of the path, here the book_id must be < 0
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')
        

# Endpoint to get all books of a select rating using query param
@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)): # Query param validation.
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

# @app.post("/create-book")
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)

# Endpoint to get books by published date
@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_published_date(published_date: int = Query(gt=0, lt=2023)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

# Endpoint to create a new book entry using the validated data from BookRequest
@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    # Debug print to show the type of book_request after validation
    print(type(book_request))  # Expected: <class 'BookRequest'>
    # Create a new Book instance from the validated data
    new_book = Book(**book_request.dict())
    # Debug print to show the type of the created Book instance
    print(type(new_book))  # Expected: <class 'Book'>
    # Add the new book to the list, assigning it a unique ID
    BOOKS.append(find_book_id(new_book))
    # Return a success message and the created book
    return {"msg": "Book created successfully!", "book": new_book}

# Endpoint to update a book using PUT
@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found.")
            

# Endpoint to delete a book by id
@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found.")

# Utility function to find a unique ID for a new book
def find_book_id(book: Book):
    # Assign ID 1 if the BOOKS list is empty, otherwise increment the last book's ID
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # Return the book with the assigned ID
    return book