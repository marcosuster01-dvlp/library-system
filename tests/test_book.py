from models.book import Book

def test_get_info():
    bk = Book("The Hobbit", "R.R. Tolkien", 2010)
    info = bk.get_info()
    assert "The Hobbit" in info
    assert "R.R. Tolkien" in info