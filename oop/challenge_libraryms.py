class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Implement the logic to add a book to the library

    def borrow_book(self, title):
        # Implement the logic to borrow a book from the library

    def return_book(self, title):
        # Implement the logic to return a book to the library

# Example Usage
library = Library()
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

# Try borrowing and returning books
