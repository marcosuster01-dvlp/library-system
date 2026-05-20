class Book:
    def __init__(self, title, author, year,):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
    
    def get_info(self):
        return f"{self.title} | {self.author} | {self.year}"
    
    def checkout(self):
        if self.is_available:
            self.is_available = False
            return "Book checked out"
        else:
            return "Book not available"
    
    def return_book(self):
        self.is_available = True
        return "Book returned successfully"

