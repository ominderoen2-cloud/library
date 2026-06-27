import psycopg2
import os 
from dotenv import load_dotenv
load_dotenv()
def connect_db():
    return psycopg2.connect(os.getenv("DATABASE_URL") , sslmode = "require")
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE IF NOT EXISTS library (id PRIMARY KEY , NAME TEXT)""")
    conn.commit()
    conn.close()
def add_member(member_id , name):
    conn = connect_db()
    cursor = conn.cursor()
    try:
      cursor.execute("INSERT INTO library (id , name) VALUES (%s,%s)", (member_id , name))
      conn.commit()
      return True
    except psycopg2.IntegrityError:
        return False
    finally:
        conn.close()
def get_all_members():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id , name FROM library")
    row = cursor.fetchall()
    conn.close()
    return{"id":row[1] , "name":row[2]}
def update_member_data(name , member_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE library SET name = %s WHERE id = %s" , (name , member_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0
def delete_member(member_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM library WHERE id = %s" , (member_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0
