class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
        return self.books
    
    def get_available_books(self):
        return [book for book in self.books if book.is_available]
    
    def search_by_author(self, author):
        return [book for book in self.books if book.author == author]
    
    def get_total_books(self):
        return len(self.books)

        