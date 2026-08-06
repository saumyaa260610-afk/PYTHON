from member import Member
class Student(Member):
    limit_borrow=3
    loan_days=15
    fine_each_day=10
    def __init__(self,user_id,name,password,"Student"):
        super().__init__(user_id,name,password)
