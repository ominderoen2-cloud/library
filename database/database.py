import psycopg2
import os 
from dotenv import load_dotenv
load_dotenv()
def connect_db():
    return psycopg2.connect(os.getenv("DATABASE_URL") , sslmode = "require")
def create_member_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS members (member_id TEXT PRIMARY KEY , NAME TEXT)""")
    conn.commit()
    conn.close()
def add_member(member_id , name):
    conn = connect_db()
    cursor = conn.cursor()
    try:
      cursor.execute("INSERT INTO members (member_id , name) VALUES (%s,%s)", (member_id , name))
      conn.commit()
      return True
    except psycopg2.IntegrityError:
        return False
    finally:
        conn.close()
def get_all_members():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT member_id , name FROM members")
    rows = cursor.fetchall()
    conn.close()
    return rows
def update_member_data(name , member_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE members SET name = %s WHERE member_id = %s" , (name , member_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0
def delete_member(member_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE  member_id = %s" , (member_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0
def add_book(book_id , book_title , author , availability):
    conn = connect_db()
    cursor = conn.cursor()
    try :
        cursor.execute("INSERT INTO books (book_id , book_title , author , availability) VALUES (%s,%s,%s,%s)" , (book_id ,  book_title, author , availability))
        conn.commit()
        return True
    
    except psycopg2.IntegrityError:
        return False
    finally:
        conn.close()
def create_borrow_books_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS borrowbooks (borrow_id TEXT PRIMARY KEY , member_id TEXT , book_id TEXT,  book_title TEXT , borrowed_at TIMESTAMP , returned_at TIMESTAMP)""")
    conn.commit()
    conn.close()
def create_books_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS books (book_id TEXT PRIMARY KEY , book_title TEXT , author TEXT , availability TEXT)""")
    conn.commit()
    conn.close()
def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0
def list_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT book_id , book_title , author , availability FROM books")
    rows = cursor.fetchall()
    return rows
def add_borrow_record(borrow_id ,member_id , book_id, book_title , borrowed_at , returned_at):
    conn = connect_db()
    cursor = conn.cursor()
    try:
       cursor.execute("INSERT INTO borrowbooks (borrow_id ,member_id, book_id , book_title, borrowed_at, returned_at ) VALUES (%s , %s , %s , %s , %s  , %s)" , (borrow_id , member_id , book_id, book_title , borrowed_at ,returned_at  ))
       conn.commit()
       return True
    except psycopg2.IntegrityError:
        return False
    finally :
        conn.close()

def add_return_record( returned_at , borrow_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE borrowbooks SET returned_at = %s WHERE borrow_id = %s", (returned_at , borrow_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0
def book_borrowed( book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET availability = 'borrowed' WHERE book_id = %s" , ( book_id,))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0
def book_returned( book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET availability = 'available' WHERE book_id = %s" , (book_id,))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return  updated > 0
def get_book_status(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT availability FROM books WHERE book_id = %s" , (book_id,))
    row = cursor.fetchone()
    conn.close()
    return row
#library/database/database.py



