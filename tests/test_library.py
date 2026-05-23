from models.library import Library
from models.book import Book

def test_add_book():
    lib = Library("My Library")
    bk = Book("The Hobbit", "R.R. Tolkien", 2010)
    lib.add_book(bk)
    assert len(lib.books) == 1
    assert lib.books[0].title == "The Hobbit"

def test_get_available_books():
    # 1. ARRANGE — biblioteca con 3 libros, uno prestado
    lib = Library("Mi Biblioteca")
    bk1 = Book("The Hobbit", "R.R. Tolkien", 2010)
    bk2 = Book("1984", "George Orwell", 1949)
    bk3 = Book("Dune", "Frank Herbert", 1965)
    lib.add_book(bk1)
    lib.add_book(bk2)
    lib.add_book(bk3)
    bk2.checkout()  # prestás el segundo

    # 2. ACT
    disponibles = lib.get_available_books()

    # 3. ASSERT — solo 2 disponibles
    assert len(disponibles) == 2

def test_search_by_author():
    # 1. ARRANGE — dos libros de Tolkien, uno de otro autor
    lib = Library("Mi Biblioteca")
    bk1 = Book("The Hobbit", "R.R. Tolkien", 2010)
    bk2 = Book("The Lord of the Rings", "R.R. Tolkien", 1954)
    bk3 = Book("1984", "George Orwell", 1949)
    lib.add_book(bk1)
    lib.add_book(bk2)
    lib.add_book(bk3)

    # 2. ACT
    resultado = lib.search_by_author("R.R. Tolkien")

    # 3. ASSERT — solo los 2 de Tolkien
    assert len(resultado) == 2