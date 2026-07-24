#STUDENT LIBRARY
class Book:
    def __init__(self,book_name,genre,book_id,language,status):
        self.book_name=book_name
        self.genre=genre
        self.book_id=book_id
        self.language=language
        self.status=status
        
    def book_details(self):
           print(f"Book name:{self.book_name}")
           print(f"Genre:{self.genre}")
           print(f"Book ID:{self.book_id}")
           print(f"Language:{self.language}")
           print(f"Status:{self.status}")

    def borrow_book(self):
            if self.status=="Available":
                print(f"{self.book_name} is Available.")
                stud_name=input("Enter your name:")
                stud_id=int(input("Enter Your Student ID:"))
                print("All set! Here are the final details:")
                print(f"Student Name:{stud_name} \nStudent ID:{stud_id} \nBook name:{self.book_name}")
                print(f"Book ID:{self.book_id}")
                print(f"Genre:{self.genre}")
                self.status="Borrowed"
                print(f"Status:{self.status} \nEnjoy Reading!")
            else:
                print(f"Sorry, {self.book_name} is not Available.")
             
    def return_book(self):
        stud_name=input("Enter student name:")
        stud_id=input("Enter student ID:")
        print(f"{self.book_name} successfully Returned. \nThank you!")
        self.status="Available"


class Library:
     def __init__(self,books):
         self.books=books
         
     def display_books(self):
         print("Here are the books available:")
         for i in self.books:
            print(i.book_name)

     def search_books(self):
        book=input("Enter book name to search for:")
        for i in self.books:
            if book==i.book_name:
                print(f"{book} is Available!")
                break
        else:
            print(f"Sorry, {book} is not Available.")

            
book1=Book("The Silent Patient","Thriller",101,"English","Available")
book2=Book("Gone Girl","Thriller",102,"English","Available")
book3=Book("The Hobbit","Fantasy",103,"English","Available")
book4=Book("Eragon","Fantasy",104,"English","Available")
book5=Book("The Maze Runner","Adventure",105,"English","Available")
book6=Book("Life of Pi","Adventure",106,"English","Available")
book7=Book("Treasure Island","Adventure",107,"English","Available")

books=[book1,book2,book3,book4,book5,book6,book7]
library=Library(books)

    
print("Hello! \nWelcome to the Student Library.")
while True:
    print('''
    1.Display all books available
    2.Search for availability of a book
    3.Details regarding a book
    4.Borrow a book
    5.Return a book
    ''')
    choice=int(input("Kindly enter a number from the above options:"))
    
    if choice==1:
        library.display_books()

    elif choice==2:
        library.search_books()

    elif choice==3:
        search=input("Enter book name:")
        for i in books:
            if search==i.book_name:
                i.book_details()
                break
        else:
            print(f"{search} not found.")

    elif choice==4:
        borrow=input("Enter the book you'd like to borrow:")
        for i in books:
            if borrow==i.book_name:
                i.borrow_book()
                break
        else:
            print(f"{borrow} not found.")
            
    elif choice==5:
        book=input("Enter the book you'd like to return:")
        for i in books:
            if book==i.book_name:
                i.return_book()
                break
        else:
            print(f"{book} not found.")
        
    else:
        print("Invalid Number.")
        
    cont=input("Would you like to continue?(yes/no):").lower()
    if cont=="no":
        exit()
        
