from book import Book 
from student import Student 
from faculty import Faculty
from librarian import Librarian
from datetime import date,timedelta
from databases import *

class Library:
    def __init__(self):
        self.books={}
        self.members={}
        self.book_titles={}
        self.book_count=100
        self.member_count=100

    def login(self,user_id,password):
        if user_id in self.members:
            member=self.members[user_id]
            if member.password==password:
                print("Login Successful")
                return member
            else:
                print("Incorrect Password")
        else:
            print("Invalid User ID")
            return None

    def add_book(self,title,author,year):
            self.book_count+=1
            book_id=self.book_count
            new_book=Book(book_id,title,author,year)
            self.books[book_id]=new_book
            self.book_titles[title.lower()]=new_book
            print("Book added successfully")
            print("Book ID:",book_id)
            add_book(book_id,title,author,year,new_book.status)
        
    def remove_book(self,book_id):
        if book_id not in self.books:
            print("Book not found")
        elif self.books[book_id].status!="Available":
            print("Book cannot be removed")
        else:
            del self.books[book_id]
            print("Book removed successfully")
            remove_book(book_id)

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
            book.borrow_date=date.today()
            book.return_by=date.today()+timedelta(days=member.loan_days)
            print("Book borrowed successfully")
            borrow_book(book_id,user_id,book.borrow_date,book.return_by)
            
    def return_book(self,user_id,book_id):
        if book_id not in self.books:
            print("Book not found")
            return
        member=self.members[user_id]
        book=self.books[book_id]
        if book_id not in member.borrowed_books:
            print("This book was not borrowed")
            return
        today=date.today()
        if today>book.return_by and member.role=="Student":
            extra_days=(today-book.return_by).days
            fine=extra_days*member.fine_each_day
            member.fine+=fine
            print("Book returned late.Fine:",fine)
        member.borrowed_books.remove(book_id)
        book.status="Available"
        book.borrowed_by=""
        book.borrow_date=""
        book.return_by=""
        print("Book returned successfully")
        return_book(book_id)

    def reserve_book(self,user_id,book_id):
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
        reserve_book(book_id,user_id,date.today())

    def add_member(self,role,name,password):
        self.member_count+=1
        user_id=self.member_count
        if role.lower()=="student":
            member=Student(user_id,name,password)
        elif role.lower()=="faculty":
            member=Faculty(user_id,name,password)
        elif role.lower()=="librarian":
            member=Librarian(user_id,name,password)
        else:
            print("Invalid role")
            return
        self.members[user_id]=member
        print("Member added")
        add_member(user_id,name,password,member.role,member.fine)

    def remove_member(self,user_id):
        if user_id not in self.members:
            print("Member not found")
        else:
            del self.members[user_id]
            print("Member removed successfully")
            remove_member(user_id)

    def search_member(self,user_id):
        if user_id in self.members:
            member=self.members[user_id]
            member.details()
        else:
            print("Member not found")

    def pay_fine(self, user_id):
        member=self.members[user_id]
        if member.role=="Student":
            if member.fine==0:
                print("No fine to be paid")
            else:
                print("fine:",member.fine)
                payment=float(input("Enter amount to pay:"))
                if payment>member.fine:
                    print("Payment amount is greater than fine.")
                elif payment<member.fine:
                    member.fine-=payment
                    print("Remaining fine:",member.fine)
                    pay_fine(user_id,payment,date.today(),member.fine)
                else:
                    print("Complete fine paid")
                    member.fine=0
                    pay_fine(user_id,payment,date.today(),member.fine)
        else:
            print("No fine")
