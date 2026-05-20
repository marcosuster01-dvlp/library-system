class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
        return self.books
        