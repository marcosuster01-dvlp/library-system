class Book:
    def __init__(self, title, author, year, is_available):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available
    
    def get_info(self):
        return f"{self.title} | {self.author} | {self.year}"
    
    def checkout(self):
        if self.is_available:
            self.is_available == False
            return "Book checked out"
        else:
            return "Book not available"

