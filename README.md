# fastapi_udemy
udemy tutorial for fastapi

initial setup and installs.
python -m venv venv
fastapi_udemy>venv\Scripts\activate

pip install fastapi
pip install "uvicorn[standard]"

uvicorn books:app --reload
uvicorn is the webserver that comes with fast api
books is refering to the books.py
app is the app = FastAPI() inside books
--reload will reload the app to reload everything there's a code change.

todoapp.
install sqlalchemy
pip install sqlalchemy