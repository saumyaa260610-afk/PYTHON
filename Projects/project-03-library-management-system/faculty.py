from member import Member
class Faculty(Member):
    limit_borrow=5
    loan_days=30
    def __init__(self,user_id,name,password):
        super().__init__(user_id,name,password,"Faculty")
