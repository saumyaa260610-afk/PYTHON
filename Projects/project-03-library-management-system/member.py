class Member:
    def __init__(self,user_id,name,password):
        self.user_id=user_id
        self.name=name
        self.password=password
        self.borrowed_books=[]
        self.reserved_books=[]
    def details(self):
        print("User ID:",self.user_id)
        print("Name:",self.name)
        print("Borrowed Books:",self.borrowed_books)
