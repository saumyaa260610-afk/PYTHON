import mysql.connector as db
dbs=db.connect(host="localhost",user="root",password="pass",database="library")
cur=dbs.cursor()
    
def create_table(query):
    cur.execute(query)
    dbs.commit()
    
table_books="""CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY,title VARCHAR(100),author VARCHAR(100),year INT,status VARCHAR(20),borrowed_by INT,borrow_date DATE,return_by DATE,reserved_by INT)"""
create_table(table_books)

table_members="""CREATE TABLE IF NOT EXISTS members(user_id INT PRIMARY KEY,name VARCHAR(100),password VARCHAR(100),role VARCHAR(20),fine DECIMAL(10,2))"""
create_table(table_members)

table_payments="""CREATE TABLE IF NOT EXISTS payments(payment_id INT PRIMARY KEY ,user_id INT,amount DECIMAL(10,2),payment_date DATE)"""
create_table(table_payments)

table_reserve="""CREATE TABLE IF NOT EXISTS reservations(reserve_id INT PRIMARY KEY ,user_id INT,book_id INT,reserve_date DATE)"""
create_table(table_reserve)
