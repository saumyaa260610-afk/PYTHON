from member import Member
class Librarian(Member):
    def __init__(self,user_id,name,password):
        super().__init__(user_id,name,password)
