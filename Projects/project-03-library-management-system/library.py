from book import Book
from student import Student
from faculty import Faculty
from librarian import Librarian
from datetime import date,timedelta
from databases import *

class Library:
    def __init__(self):
        self.book_count=100
        self.member_count=100

    def login(self,user_id,password):
        member=get_member(user_id)
        if member:
            if member[2]==password:
                print("Login successful")
                return member
            else:
                print("Incorrect password")
        else:
            print("Invalid userID")
        return None

    def add_book(self,title,author,year):
        self.book_count+=1
        book_id=self.book_count
        add_book(book_id,title,author,year,"Available")
        print("Book added")
        print("Book ID:",book_id)

    def remove_book(self,book_id):
        book=get_book(book_id)
        if book==None:
            print("Book not found")
        elif book[4]!="Available":
            print("Book is not available")
        else:
            remove_book(book_id)
            print("Book removed successfully")

    def search_book_id(self,book_id):
        book=get_book(book_id)
        if book:
            print(book)
        else:
            print("Book not found")

    def search_book_title(self,title):
        book=get_book_title(title)
        if book:
            print(book)
        else:
            print("Book not found")

    def display_books(self):
        books=get_all_books()
        for book in books:
            print(book)

    def borrow_book(self,user_id,book_id):
        book=get_book(book_id)
        member=get_member(user_id)
        if book==None:
            print("Book not found")
            return
        if book[4]!="Available":
            print("Book not available")
            return
        if member[3]=="Student":
            borrowed_books=0
            if count_borrowed_books(user_id)>=Student.limit_borrow:
                print("Borrowing limit reached")
                return
            loan_days=Student.loan_days
        elif member[3]=="Faculty":
            loan_days=Faculty.loan_days
        else:
            print("Librarians cannot borrow books")
            return
        borrow_date=date.today()
        return_by=borrow_date+timedelta(days=loan_days)
        borrow_book(book_id,user_id,borrow_date,return_by)
        print("Book borrowed successfully")

    def return_book(self,user_id,book_id):
        book=get_book(book_id)
        member=get_member(user_id)
        if book==None:
            print("Book not found")
            return
        if book[5]!=user_id:
            print("This book was not borrowed")
            return
        today=date.today()
        if today>book[7] and member[3]=="Student":
            extra_days=(today-book[7]).days
            fine=extra_days*Student.fine_each_day
            new_fine=float(member[4])+fine
            update_member(user_id,member[1],member[2],member[3],new_fine)
            print("Book returned late. Fine:",fine)
        return_book(book_id)
        print("Book returned successfully")
        
    def reserve_book(self,user_id,book_id):
        book=get_book(book_id)
        if book==None:
            print("Book not found")
            return
        if book[8]!=None:
            print("Book is already reserved")
            return
        reserve_book(book_id,user_id,date.today())
        print("Book reserved successfully")

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
        add_member(user_id,name,password,member.role,member.fine)
        print("Member added")
        print("User ID:",user_id)

    def remove_member(self,user_id):
        member=get_member(user_id)
        if member==None:
            print("Member not found")
        else:
            remove_member(user_id)
            print("Member removed successfully")

    def search_member(self,user_id):
        member=get_member(user_id)
        if member:
            print("userID:",member[0])
            print("Name:",member[1])
            print("Role:",member[3])
            print("fine:",member[4])
        else:
            print("Member not found")

    def display_members(self):
        members=get_all_members()
        for member in members:
            print(member)

    def pay_fine(self,user_id):
        member=get_member(user_id)
        if member==None:
            print("Member not found")
            return
        if member[3]!="Student":
            print("No fine")
            return
        if member[4]==0:
            print("No fine to be paid")
            return
        print("Fine:",member[4])
        payment=float(input("Enter amount to pay:"))
        if payment>member[4]:
            print("Payment amount is greater than fine.")
        elif payment<member[4]:
            remaining_fine=float(member[4])-payment
            pay_fine(user_id,payment,remaining_fine)
            print("Remaining fine:",remaining_fine)
        else:
            pay_fine(user_id,payment,0)
            print("Complete fine paid")
            
