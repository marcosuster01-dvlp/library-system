from models.library import Library
from models.book import Book

def test_add_book():
    lib = Library("My Library")
    bk = Book("The Hobbit", "R.R. Tolkien", 2010)
    lib.add_book(bk)
    assert len(lib.books) == 1
    assert lib.books[0].title == "The Hobbit"