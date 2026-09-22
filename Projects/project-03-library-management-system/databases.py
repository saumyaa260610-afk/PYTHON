import mysql.connector as db
from datetime import date
dbs=db.connect(host="localhost",user="root",password="pass",database="library")
cur=dbs.cursor()

def create_table(query):
    cur.execute(query)
    dbs.commit()

table_books="""CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY,title VARCHAR(100),author VARCHAR(100),year INT,status VARCHAR(20),borrowed_by INT,borrow_date DATE,return_by DATE,reserved_by INT)"""
create_table(table_books)

table_members="""CREATE TABLE IF NOT EXISTS members(user_id INT PRIMARY KEY,name VARCHAR(100),password VARCHAR(100),role VARCHAR(20),fine DECIMAL(10,2))"""
create_table(table_members)

table_payments="""CREATE TABLE IF NOT EXISTS payments(payment_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT,amount DECIMAL(10,2),payment_date DATE)"""
create_table(table_payments)

table_reserve="""CREATE TABLE IF NOT EXISTS reserve(reserve_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT,book_id INT,reserve_date DATE)"""
create_table(table_reserve)

def add_book(book_id,title,author,year,status):
    query="""INSERT INTO books(book_id,title,author,year,status) VALUES (%s,%s,%s,%s,%s)"""
    cur.execute(query,(book_id,title,author,year,status))
    dbs.commit()

def remove_book(book_id):
    query="DELETE FROM books WHERE book_id=%s"
    cur.execute(query,(book_id,))
    dbs.commit()

def add_member(user_id,name,password,role,fine):
    query="""INSERT INTO members(user_id,name,password,role,fine) VALUES (%s,%s,%s,%s,%s)"""
    cur.execute(query,(user_id,name,password,role,fine))
    dbs.commit()

def remove_member(user_id):
    query="DELETE FROM members WHERE user_id=%s"
    cur.execute(query,(user_id,))
    dbs.commit()

def update_book(book_id,title,author,year):
    query="""UPDATE books SET title=%s,author=%s,year=%s WHERE book_id=%s"""
    cur.execute(query,(title,author,year,book_id))
    dbs.commit()

def update_member(user_id,name,password,role,fine):
    query="""UPDATE members SET name=%s,password=%s,role=%s,fine=%s WHERE user_id=%s"""
    cur.execute(query,(name,password,role,fine,user_id))
    dbs.commit()

def get_book(book_id):
    query="""SELECT * FROM books WHERE book_id=%s"""
    cur.execute(query,(book_id,))
    return cur.fetchone()

def get_all_books():
    query="""SELECT * FROM books"""
    cur.execute(query)
    return cur.fetchall()

def get_member(user_id):
    query="""SELECT * FROM members WHERE user_id=%s"""
    cur.execute(query,(user_id,))
    return cur.fetchone()

def get_all_members():
    query="""SELECT * FROM members"""
    cur.execute(query)
    return cur.fetchall()

def get_book_title(title):
    query="SELECT * FROM books WHERE title=%s"
    cur.execute(query,(title,))
    return cur.fetchone()

def borrow_book(book_id,user_id,borrow_date,return_by):
    query="""UPDATE books SET status=%s,borrowed_by=%s,borrow_date=%s,return_by=%s WHERE book_id=%s"""
    cur.execute(query,("Borrowed",user_id,borrow_date,return_by,book_id))
    dbs.commit()

def return_book(book_id):
    query="""UPDATE books SET status=%s,borrowed_by=%s,borrow_date=%s,return_by=%s WHERE book_id=%s"""
    cur.execute(query,("Available",None,None,None,book_id))
    dbs.commit()

def reserve_book(book_id,user_id,reserve_date):
    query="""INSERT INTO reserve(user_id,book_id,reserve_date) VALUES(%s,%s,%s)"""
    cur.execute(query,(user_id,book_id,reserve_date))
    dbs.commit()

def pay_fine(user_id,payment,remaining_fine):
    query="""INSERT INTO payments(user_id,amount,payment_date) VALUES(%s,%s,%s)"""
    cur.execute(query,(user_id,payment,date.today()))
    query="UPDATE members SET fine=%s WHERE user_id=%s"
    cur.execute(query,(remaining_fine,user_id))
    dbs.commit()
