from library import Library
library=Library()
library.load()
print("WELCOME TO THE LIBRARY!")
user_id=int(input("Enter User ID:"))
password=input("Enter Password:")
member=library.login(user_id,password)
if member!=None:
    while True:
        if member.role=="Student" or member.role=="Faculty":
            print(f'''{member.role.upper()} MENU:\n1.Borrow Book\n2.Return Book\n3.Reserve Book\n4.Search Book\n5.Account Summary\n6.Fine payment\n7.Logout''')
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
                library.pay_fine(user_id)
            elif choice==7:
                print("Logged out")
                
        elif member.role=="Librarian":
            print('''LIBRARIAN MENU:\n1.Add Book\n2.Remove Book\n3.Display Books\n4.Add Member\n5.Remove Member\n6.Search Member\n7.Search Books\n8.Logout''')
            choice=int(input("Enter choice:"))
            if choice==1:
                title=input("Enter book title:")
                author=input("Enter Author name:")
                year=input("Enter year of release:")
                library.add_book(title,author,year)
            elif choice==2:
                book_id=int(input("Enter Book ID:"))
                library.remove_book(book_id)
            elif choice==3:
                library.display_books()
            elif choice==4:
                role=input("Enter role:")
                name=input("Enter name of member:")
                password=input("Enter password:")
                library.add_member(role,name,password)
            elif choice==5:
                user_id=int(input("Enter user ID of member:"))
                library.remove_member(user_id)
            elif choice==6:
                user_id=int(input("Enter user ID of member:"))
                library.search_member(user_id)
            elif choice==7:
                choice=int(input("Would you like to search by: \n 1.ID or \n 2.Title ?"))
                if choice==1:
                    book_id=int(input("Enter Book ID:"))
                    library.search_book_id(book_id)
                elif choice==2:
                    title=input("Enter book title:")
                    library.search_book_title(title)
            elif choice==8:
                print("Logged Out")
elif choice==2:
    print("Exited the Library")
else:
    print("Invalid choice")

cont=input("Would you like to continue? (yes or no) \n")
if cont.lower()=="no":
    library.save()
    break
