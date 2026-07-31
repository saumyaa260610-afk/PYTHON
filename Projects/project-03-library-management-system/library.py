from book import Book 
from student import Student 
from faculty import Faculty
from librarian import Librarian
class Library:
    def __init__(self):
        self.books={}
        self.members={}
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
        for book in self.books.values():
            if book.title.lower() == title.lower():
                print(book)
                return
        else:
            print("Book not found.")

    def display_books(self):
        for book in self.books.values():
                print(book)    
