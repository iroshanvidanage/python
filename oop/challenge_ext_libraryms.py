class Member:
    def __init__(self, name: str, member_id: str) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book) -> None:
        # Implement the logic to borrow a book

    def return_book(self, book) -> None:
        # Implement the logic to return a book

    def __str__(self) -> str:
        return f'Member(name={self.name}, member_id={self.member_id})'

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self) -> str:
        return f'Book(title={self.title}, author={self.author})'

class Library:
    def __init__(self) -> None:
        self.books = []
        self.members = []

    def add_book(self, book: Book) -> None:
        # Implement the logic to add a book to the library

    def register_member(self, member: Member) -> None:
        # Implement the logic to register a member

    def reserve_book(self, book: Book, member: Member) -> None:
        # Implement the logic to reserve a book

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

    print(library)

if __name__ == '__main__':
    test_example()
