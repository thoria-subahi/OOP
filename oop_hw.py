'''
 Excercise: Build a Simple Library System

Let's build a simple library system using Object-Oriented Programming (OOP) principles in Python. This system will manage books and library members, allowing members to borrow and return books.

**Tasks**

1. Define Classes:

* Create a Book class to represent individual books with attributes such as title, author, and availability status.

* Design a Member class to model library members with attributes like name, member ID, and borrowed books.

* Implement a Library class to manage the library's collection of books and members.

2. Implement Class Methods:

* Add methods to the Library class for adding books to the collection and registering members.

* Include methods in the Library class for lending books to members and processing book returns.


'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"




class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}"



class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{book.title} lent to {member.name}")
        else:
            print(f"Sorry, {book.title} is not available to lend")
    
    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{book.title} has been returned by {member.name}")
        else:
            print(f"{member.name} has not borrowed {book.title}")