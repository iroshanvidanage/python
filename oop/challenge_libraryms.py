class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        # Implement the logic to add a book to the library
        self.books.append(book)
        print(f'The {book.title} is added to library')
    
    def find_book(self, title: str):
        return next((book for book in self.books if book.title == title), None)
    
# implementation
    def borrow_book(self, title: str):
        # Implement the logic to borrow a book from the library
        book = self.find_book(title)
        if book is None:
            print(f'The book "{title}" is not available')
        elif book.is_borrowed:
            print('This book is already borrowed')
        else:
            book.is_borrowed = True
            print('Succesfully borrowed the book')


    def return_book(self, title: str):
        # Implement the logic to return a book to the library
        book = self.find_book(title)
        if book is None:
            print(f'The book "{title}" is not this library\'s asset')
        else:
            book.is_borrowed = False
            print('Succesfully returned the book')

'''
# original implementation

    def borrow_book(self, title: Book):
        # Implement the logic to borrow a book from the library
        if title not in self.books:
            print('This book is not available')
        elif title.is_borrowed:
            print('This book is already borrowed')
        else:
            title.is_borrowed = True
            print('Succesfully borrowed the book')

    def return_book(self, title: Book):
        # Implement the logic to return a book to the library
        if title not in self.books:
            print('This book is not this library\'s asset')
        else:
            title.is_borrowed = False
            print('Succesfully returned the book')

'''


# Example Usage
library = Library()
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

# Try borrowing and returning books
# library.borrow_book(book1)
# library.borrow_book(book1)
# library.borrow_book(book2)

# library.return_book(book1)
# library.return_book(book2)
library.borrow_book("The Catcher in the Rye")
library.borrow_book("The Catcher in the Rye")
library.borrow_book("To Kill a Mockingbird")

library.return_book("The Catcher in the Rye")
library.return_book("To Kill a Mockingbird")
library.return_book("Jade Compass")