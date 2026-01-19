from fastapi import FastAPI

app = FastAPI()

BOOKS  = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 4, "title": "Moby", "author": "Herman Melville"},
    {"id": 5, "title": "War and Peace", "author": "Leo Tolstoy"},
    {"id": 6, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 7, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},  
     
     ]

for book in BOOKS:
    print(f"Book ID: {book["id"]}, Title: {book['title']}, Author: {book['author']}")   


@app.get("/{boi_no}")
def books(boi_no: int): # boi_no holo path parameter
                        # boi_no er maddhome specific book er information return korbe
    for book in BOOKS:
        if book["id"] == boi_no:
            return book
    return {"error": "Book not found NOOO"}
