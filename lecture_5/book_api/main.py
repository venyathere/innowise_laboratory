from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import update, delete, or_, and_, select
from fastapi import FastAPI

engine = create_engine('sqlite:///books.db')

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=True)


Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

#Get a list of books
@app.get("/books/")
async def get_books():
    books = session.query(Book).all()
    return books

#Add a new book
@app.post("/books/")
async def add_book(title: str, author: str, year: int | None = None):
    book = Book(title=title, author=author, year=year)
    session.add(book)
    session.commit()

#Update book details
@app.post("/books/{book_id}")
async def update_book(book_id: int, title: str | None = None, author: str | None = None, year: int | None = None):
    book = session.query(Book).filter_by(id=book_id).one_or_none()
    old_title = book.title
    old_author = book.author
    old_year = book.year

    if title == None:
        book.title = old_title
    else:
        book.title = title

    if author == None:
        book.author = old_author
    else:
        book.author = author
    
    if year == None:
        book.year = old_year
    else:
        book.year = year

    session.commit()

#Delete a book
@app.post("/books/{book_id}")
async def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).one_or_none()
    session.delete(book)
    session.commit()

#Search for books
@app.post("/books/search/")
async def search(title: str | None = None, author: str | None = None, year: int | None = None):
    conditons = []
    if title is not None:
        conditons.append(Book.title == title)
    if author is not None:
        conditons.append(Book.author == author)
    if year is not None:
        conditons.append(Book.year == year)
    
    if not conditons:
        return []
    
    stmt = select(Book).where(or_(*conditons))

    results = session.execute(stmt).scalars().all()
    return results