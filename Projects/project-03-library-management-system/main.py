from library import Library
inputs=[]
def parser(text):
    inputs.extend(str(text).split())
    
library=Library()
library.load()
library.add_member("student","saumyaa",1234)
while True:
    print('''WELCOME TO THE LIBRARY!
    1.Login
    2.Exit''')
    choice=int(input("Enter choice:"))
    parser(choice)
    if choice==1:
        user_id=int(input("Enter User ID:"))
        password=input("Enter Password:")
        parser(user_id)
        parser(password)
        member=library.login(user_id,password)
        if member!=None:
            if member.role=="Student" or member.role=="Faculty":
                print(f'''{member.role.upper()} MENU:
                1.Borrow Book
                2.Return Book
                3.Reserve Book
                4.Search Book
                5.Account Summary
                6.Fine payment
                7.Logout''')
                choice=int(input("Enter choice:"))
                parser(choice)
                if choice==1:
                    book_id=int(input("Enter Book ID:"))
                    parser(book_id)
                    library.borrow_book(user_id,book_id)
                elif choice==2:
                    book_id=int(input("Enter Book ID:"))
                    parser(book_id)
                    library.return_book(user_id,book_id)
                elif choice==3:
                    book_id=int(input("Enter Book ID:"))
                    parser(book_id)
                    library.reserve_book(user_id,book_id)
                elif choice==4:
                    choice=int(input("Would you like to search by: \n 1.ID or \n 2.Title ?"))
                    parser(choice)
                    if choice==1:
                        book_id=int(input("Enter Book ID:"))
                        parser(book_id)
                        library.search_book_id(book_id)
                    elif choice==2:
                        title=input("Enter book title:")
                        parser(title)
                        library.search_book_title(title)
                elif choice==5:
                    member.account_summary()
                elif choice==6:
                    library.pay_fine(user_id)
                elif choice==7:
                    print("Logged out")
                    
            elif member.role=="Librarian":
                print('''LIBRARIAN MENU:
                1.Add Book
                2.Remove Book
                3.Display Books
                4.Remove Member
                5.Search Member
                6.Search Books
                7.Logout''')
                choice=int(input("Enter choice:"))
                parser(choice)
                if choice==1:
                    title=input("Enter book title:")
                    author=input("Enter Author name:")
                    year=input("Enter year of release:")
                    parser(title)
                    parser(author)
                    parser(year)
                    library.add_book(title,author,year)
                elif choice==2:
                    book_id=int(input("Enter Book ID:"))
                    parser(book_id)
                    library.remove_book(book_id)
                elif choice==3:
                    library.display_books()
                elif choice==4:
                    user_id=int(input("Enter user ID of member:"))
                    parser(user_id)
                    library.remove_member(user_id)
                elif choice==5:
                    user_id=int(input("Enter user ID of member:"))
                    parser(user_id)
                    library.search_member(user_id)
                elif choice==6:
                    choice=int(input("Would you like to search by: \n 1.ID or \n 2.Title ?"))
                    parser(choice)
                    if choice==1:
                        book_id=int(input("Enter Book ID:"))
                        parser(book_id)
                        library.search_book_id(book_id)
                    elif choice==2:
                        title=input("Enter book title:")
                        parser(title)
                        library.search_book_title(title)
                elif choice==7:
                    print("Logged Out")
    elif choice==2:
        print("Exited the Library")
    else:
        print("Invalid choice")

    cont=input("Would you like to continue? (yes or no) \n")
    parser(cont)
    if cont.lower()=="no":
        library.save()
        print(inputs)
        break
