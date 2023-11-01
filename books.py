from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'title 1', 'author': 'author 1', 'category': 'science'},
    {'title': 'title 2', 'author': 'author 2', 'category': 'science'},
    {'title': 'title 3', 'author': 'author 3', 'category': 'history'},
    {'title': 'title 4', 'author': 'author 4', 'category': 'math'},
    {'title': 'title 5', 'author': 'author 5', 'category': 'math'},
]

"""
    GET REQUESTS
"""

@app.get("/test")
async def first_api():
    return {'message': 'Hello World!'}

@app.get("/books")
async def read_all_books():
    return BOOKS

# a static param like /mybook will need to be above the dynamic param. or it'll never get called
@app.get("/books/mybook") 
async def read_all_books():
    return {'book_title': 'My Favorite Book'}

# Path Parameters
# URL: 127.0.0.1:8000/books/title%204   # the %20 is like a space.
@app.get("/books/{book_title}")
async def read_all_books_param(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# Query Paramters
# URL: 127.0.0.1.8000/?category=science
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Query Parameters (and Path Parameters)
# URL: 127.0.0.1:8000/books/author%201/?category=science
@app.get("/books/{book_author}/")
async def read_category_by_path_and_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

""" 
    POST REQUESTS 
"""
#import body from fastapi

@app.post("/books/create_book")
async def create_book(new_book=Body()): # the Body() can be seen on swagger, "Request Body". it's where you'll type the json to pass to the endpoint.
    BOOKS.append(new_book)

"""
    PUT REQUESTS
"""

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book