from library import Library
library=Library()
library.load()
while True:
    print('''WELCOME TO THE LIBRARY!
    1.Login
    2.Exit''')
    choice=int(input("Enter choice:"))
    if choice==1:
        user_id=input("Enter User ID:")
        password=input("Enter Password:")
        member=library.login(user_id,password)
        
        if member.role=="Student" or member.role=="Faculty":
            print(f'''{member.role.upper()} MENU:
            1.Borrow Book
            2.Return Book
            3.Reserve Book
            4.Search Book
            5.Account Summary
            6.Logout''')
            choice=int(input("Enter choice:"))
            if choice==1:
                book_id=int(input("Enter Book ID:"))
                library.borrow_book(user_id,book_id)
            elif choice==2:
                book_id=int(input("Enter Book ID:"))
                library.return_book(user_id,book_id)
            elif choice==3:
                book_id=int(input("Enter Book ID:"))
                library.reserve_book(user_id,book_id)
            elif choice==4:
                choice=int(input("Would you like to search by: \n 1.ID or \n 2.Title ?"))
                if choice==1:
                    book_id=int(input("Enter Book ID:"))
                    library.search_book_id(book_id)
                elif choice==2:
                    title=input("Enter book title:")
                    library.search_book_title(title)
            elif choice==5:
                member.account_summary()
            elif choice==6:
                print("Logged Out")
                
        elif member.role=="Librarian":
            print('''LIBRARIAN MENU:
            1.Add Book
            2.Remove Book
            3.Display Books
            4.Remove Member
            5.Search Member
            6.Fine Mangagement
            7.Search Books
            8.Logout''')
                
    elif choice==2:
        print("Exited the Library")
        break
