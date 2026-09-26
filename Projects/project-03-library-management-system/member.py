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
