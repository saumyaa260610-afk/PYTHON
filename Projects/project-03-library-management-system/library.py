from book import Book 
from student import Student 
from faculty import Faculty
from librarian import Librarian
class Library:
    def __init__(self):
        self.books={}
        self.members={}
        self.book_titles={}
        self.book_count=100
        self.student_count=100
        self.faculty_count=100
        self.librarian_count=100

    def login(self,user_id,password):
        if user_id in self.members:
            member=self.members[user_id]
            if member.password==password:
                print("Login Successful")
            else:
                print("Incorrect Password")
        else:
            print("Invalid User ID")

    def add_book(self,title,author,year):
            self.book_count+=1
            book_id=self.book_count
            new_book=Book(book_id,title,author,year)
            self.books[book_id]=new_book
            self.book_titles[title.lower()]=new_book
            print("Book added successfully")
            print("Book ID:",book_id)
            
    def remove_book(self,book_id):
        if book_id not in self.books:
            print("Book not found")
        elif self.books[book_id].status!="Available":
            print("Book cannot be removed")
        else:
            del self.books[book_id]
            print("Book removed successfully")

    def search_book_id(self,book_id):
        if book_id in self.books:
            print(self.books[book_id])
        else:
            print("Book not found")

    def search_book_title(self,title):
       if title.lower() in self.book_titles:
            print(self.book_titles[title.lower()])
        else:
            print("Book not found.")

    def display_books(self):
        for book in self.books.values():
                print(book)    

    def borrow_book(self,user_id,book_id):
            if user_id not in self.members:
                print("Member not found")
                return
            if book_id not in self.books:
                print("Book not found")
                return
            member=self.members[user_id]
            book=self.books[book_id]
            if book.status!="Available":
                print("Book is not available")
                return
            if len(member.borrowed_books)>=member.limit_borrow:
                print("Borrowing limit reached")
                return
            member.borrowed_books.append(book_id)
            book.status="Borrowed"
            book.borrowed_by=user_id
            print("Book borrowed successfully")
            
        def return_book(self,user_id,book_id):
            if user_id not in self.members:
                print("Member not found")
                return
            if book_id not in self.books:
                print("Book not found")
                return
            member=self.members[user_id]
            book=self.books[book_id]
            if book_id not in member.borrowed_books:
                print("This book was not borrowed")
                return
            member.borrowed_books.remove(book_id)
            book.status="Available"
            book.borrowed_by=""
            print("Book returned successfully")
    
        def reserve_book(self,user_id,book_id):
            if user_id not in self.members:
                print("Member not found")
                return
            if book_id not in self.books:
                print("Book not found")
                return
            member=self.members[user_id]
            book=self.books[book_id]
            if book.reserved_by!="":
                print("Book is already reserved")
                return
            book.reserved_by=user_id
            member.reserved_books.append(book_id)
            print("Book reserved successfully")
