class Member:
    def __init__(self,user_id,name,password,role):
        self.user_id=user_id
        self.name=name
        self.password=password
        self.role=role
        self.borrowed_books=[]
        self.reserved_books=[]
        self.fine=0
    def details(self):
        print("User ID:",self.user_id)
        print("Name:",self.name)
        print("Borrowed Books:",self.borrowed_books)
    def account_summary(self):
        print("User ID:",self.user_id)
        print("Name:",self.name)
        print("Number of borrowed books:",len(self.borrowed_books))
        print("Borrowed books:",self.borrowed_books)
        print("Number of reserved books:",len(self.reserved_books))
        print("Reserved books:",self.reserved_books)
        if self.role=="Student":
            print("Fine:",self.fine)
        else:
            print("Fine:No Fine")
