from models.book import Book

def test_get_info():
    bk = Book("The Hobbit", "R.R. Tolkien", 2010)
    info = bk.get_info()
    assert "The Hobbit" in info
    assert "R.R. Tolkien" in info

def test_checkout():
    bk = Book("The Hobbit", "R.R. Tolkien", 2010)
    bk.checkout()
    assert bk.is_available == False

def test_checkout_not_available():
    bk = Book("The Hobbit", "R.R. Tolkien", 2010)
    bk.checkout()

    not_available = bk.checkout()
    assert not_available == "Book not available"

def test_return_book():
    bk = Book("The Hobbit", "R.R. Tolkien", 2010)
    bk.checkout()
    bk.return_book()
    assert bk.is_available == True