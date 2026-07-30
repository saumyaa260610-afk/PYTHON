class Book:
    def __init__(self,title,author,year,book_id):
        self.title=title
        self.author=author
        self.year=year
        self.book_id=book_id
        self.status="Available"
        self.borrowed_by=""
        self.borrow_date=""
        self.return_by=""
        self.reserved_by=""
    def __str__(self):
       return f"{self.book_id},{self.title},{self.author},{self.status}"
