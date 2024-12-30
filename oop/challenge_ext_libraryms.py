from __future__ import annotations
from typing import List

class Member:
    def __init__(self, name: str, member_id: str) -> None:
        self.name = name
        self.member_id = member_id
        # self.borrowed_books = []
        self.borrowed_books = set()
    
    def is_book_borrowed(self, book: Book) -> bool:
        return book.title in self.borrowed_books

    def borrow_book(self, book: Book) -> None:
        # Implement the logic to borrow a book
        if self.is_book_borrowed(book):
            print(f'The book {book.title} is already borrowed.')
            return
        if book.is_borrowed:
            print(f'The book {book.title} is not available to borrow.')
            return
        if book.is_reserved and (book.reserved_member != self.member_id):
            print(f'This book is reserved by another member.')
        self.borrowed_books.add(book.title)
        book.is_borrowed = True
        book.is_reserved = False
        book.reserved_member = None
        print(f'Successfully borrowed the book {book.title}')

    def return_book(self, book: Book) -> None:
        # Implement the logic to return a book
        if not self.is_book_borrowed(book):
            print(f'This book {book.title} is not in your borrowed list.')
            return
        self.borrowed_books.remove(book.title)
        book.is_borrowed = False
        print(f'Successfully returned the book {book.title}')

    def __str__(self) -> str:
        return f'Member(name={self.name}, member_id={self.member_id})'

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.is_reserved = False
        self.reserved_member = None

    def __str__(self) -> str:
        return f'Book(title={self.title}, author={self.author})'

class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []
        self.members: List[Member] = []
    
    def is_book_available(self, book: Book) -> bool:
        return any(lbook for lbook in self.books if lbook.title == book.title)
    
    def is_member_available(self, member: Member) -> bool:
        return any(lmember for lmember in self.members if lmember.member_id == member.member_id)

    def add_book(self, book: Book) -> None:
        # Implement the logic to add a book to the library
        if self.is_book_available(book):
            print(f'The book {book.title} is already in the list.')
            return
        self.books.append(book)
        print(f'Successfully added the book {book.title} to the library catalog')

    def register_member(self, member: Member) -> None:
        # Implement the logic to register a member
        if self.is_member_available(member):
            print(f'The member {member.name}, {member.member_id} is already registered')
            return
        self.members.append(member)
        print(f'Successfully registered {member.name} to the library')

    def reserve_book(self, book: Book, member: Member) -> None:
        # Implement the logic to reserve a book
        if member.is_book_borrowed(book):
            print(f'This book is already borrowed by you')
            return
        if book.is_reserved:
            print(f'This book {book.title} is not available to reserve.')
            return
        if not book.is_borrowed:
            print(f'The book {book.title} is available to borrow.')
            member.borrow_book(book)
            return
        book.is_reserved = True
        book.reserved_member = member.member_id
        print(f'Successfully reserved the book {book.title}.')

    def __str__(self) -> str:
        return f'Library(books={len(self.books)}, members={len(self.members)})'

# Example Usage
def test_example() -> None:
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    member1 = Member("John", "M001")
    member2 = Member("Jane", "M002")

    library.add_book(book1)
    library.add_book(book2)

    library.register_member(member1)
    library.register_member(member2)

    member1.borrow_book(book1)
    member2.borrow_book(book2)

    library.reserve_book(book1, member2)

    member2.borrow_book(book1)
    member1.return_book(book1)
    library.reserve_book(book1, member1)
    member2.borrow_book(book1)

    member2.return_book(book2)
    library.reserve_book(book2, member1)
    member2.return_book(book1)
    member1.return_book(book2)

    print(library)

if __name__ == '__main__':
    test_example()
