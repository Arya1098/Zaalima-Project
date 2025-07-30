class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_limit(self):
        return 0

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit():
            print("Borrowing limit reached.")
        elif book.available_copies == 0:
            print("No copies available to borrow.")
        else:
            book.available_copies -= 1
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available_copies += 1
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print("This book is not in your borrowed list.")

    def show_borrowed_books(self):
        if not self.borrowed_books:
            print("No borrowed books.")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")

class Student(Member):
    def borrow_limit(self):
        return 3

class Faculty(Member):
    def borrow_limit(self):
        return 5

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, copies):
        for book in self.books:
            if book.title == title and book.author == author:
                book.total_copies += copies
                book.available_copies += copies
                print("More copies added.")
                return
        new_book = Book(title, author, copies)
        self.books.append(new_book)
        print("Book added.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered with ID {member.member_id}.")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

library = Library()
library.add_book("Python Basics", "John Smith", 2)
library.add_book("Data Structures", "Jane Doe", 1)
student1 = Student("Alice", "S001")
faculty1 = Faculty("Dr. Bob", "F001")
library.register_member(student1)
library.register_member(faculty1)
book1 = library.find_book_by_title("Python Basics")
if book1:
    student1.borrow_book(book1)
book2 = library.find_book_by_title("Data Structures")
if book2:
    faculty1.borrow_book(book2)
student1.borrow_book(book1)
student1.borrow_book(book1)
student1.borrow_book(book1)
student1.return_book(book1)
print("\nAlice's borrowed books:")
student1.show_borrowed_books()
print("\nDr. Bob's borrowed books:")
faculty1.show_borrowed_books()

