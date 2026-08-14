from book import Book 
from student import Student 
from faculty import Faculty
from librarian import Librarian
import json 
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

    def add_member(self,role,name,password):
        if role.lower()=="student":
            self.student_count+=1
            user_id = self.student_count
            member = Student(user_id, name, password)
        elif role.lower()=="faculty":
            self.faculty_count+=1
            user_id = self.faculty_count
            member = Faculty(user_id, name, password)
        elif role.lower()=="librarian":
            self.librarian_count+=1
            user_id=self.librarian_count
            member=Librarian(user_id, name, password)
        else:
            print("Invalid role")
            return
        self.members[user_id]=member
        print("Member added successfully")

    def remove_member(self,user_id):
        if user_id not in self.members:
            print("Member not found")
        else:
            del self.members[user_id]
            print("Member removed successfully")

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
                print("No fine")
            else:
                print("Fine:",member.fine)
                print("Fine paid")
                member.fine=0
        else:
            print("No fine")
        
    def save(self):
        all_data={}
        all_data["books"]={}
        all_data["members"]={}
        for book_id,book in self.books.items():
            all_data["books"][book_id] = {"title":book.title,"author":book.author,"year":book.year,"status":book.status,"borrowed_by":book.borrowed_by,"borrow_date":book.borrow_date,"return_by":book.return_by,"reserved_by": book.reserved_by}
        for user_id,member in self.members.items():
            all_data["members"][user_id]={"name":member.name,"password":member.password,"role": member.role,"borrowed_books":member.borrowed_books,"reserved_books":member.reserved_books,"fine": member.fine}
        with open("library.json", "w") as f:
            json.dump(all_data,f,indent=4)
            print("Data saved")
            
    def load(self):
        with open("library.json","r") as f:
            all_data=json.load(f)
        for book_id,book_data in all_data["books"].items():
            book_id=int(book_id)
            book=Book(book_data["title"],book_data["author"],book_data["year"],book_id)
            book.status=book_data["status"]
            book.borrowed_by=book_data["borrowed_by"]
            book.borrow_date=book_data["borrow_date"]
            book.return_by=book_data["return_by"]
            book.reserved_by=book_data["reserved_by"]
            self.books[book_id] = book
            self.book_titles[book.title.lower()] = book
        for user_id,member_data in all_data["members"].items():
            user_id=int(user_id)
            if member_data["role"]=="Student":
                member=Student(user_id,member_data["name"],member_data["password"])
            elif member_data["role"]=="Faculty":
                member=Faculty(user_id,member_data["name"],member_data["password"])
            else:
                member=Librarian(user_id,member_data["name"],member_data["password"])
            member.borrowed_books=member_data["borrowed_books"]
            member.reserved_books=member_data["reserved_books"]
            member.fine=member_data["fine"]
            self.members[user_id]=member
        print("Data loaded")
