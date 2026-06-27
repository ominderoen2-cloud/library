from validators.validators import validate_library_data
from database.database import add_member , get_all_members , update_member_data , delete_member, connect_db
books = []
members = []
def create_member(data):
    clean_data = validate_library_data(data)
    success = add_member(clean_data["id"] , clean_data["name"])
    if not success :
        return {"message":"member not registered"}, 409
    return {"message":"member successfully registered"} , 201
def list_members():
    return get_all_members() , 200
def remove_member(member_id):
    success = delete_member(member_id)
    if not success:
        return {"message":"user not found"} , 404
    return {"message":"successfully deleted"} , 200
def update_member(data , member_id):
    clean_data = validate_library_data(data)
    success = update_member_data(clean_data["name"] , member_id)
    if not success:
        return {"message":"member not updated"},400
    if not success:
        return {"message":"member successfully updated"} , 200
def get_by_id(member_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id , name FROM library WHERE id = %s" , (member_id,))
    row = cursor.fetchone()
    if row is None :
        return {"message":"member not found"} , 404
    return {"id":row[0] , "name":row[1]} , 200
def get_all_books():
    if books is None :
        return {"message":"no books available"}, 404
    return books , 200
def get_one_book():
    book_title = input("book tile:")
    for book in books:
        if book["book title"] == book_title:
            return print(book_title , "found"),200
        else :
            return {"message":"book not found"},404
    return {"message":"no books found"}, 404
def borrow_book():
    book_title = input("booktitle:")
    for book in books:
     member_id = input(" id:")
     for member in members:
        if member["id"] == member_id:
            if member["borrowed_books"] is None:
                member["borrowed_books"].append(book[book_title])
                return {"message":"book successfully borrowed"},200
            return{"message":"youre not eligible for borrowing . please return books you borrowed"},400
        return {"message":"wrong credentials"},400
     return {"message":"member not found"},404
def return_book():
    member_id = input(" id:")
    for member in members:
        if member["id"] == member_id:
            book_borrowed = input("booktitle:")
            if member["borrowed_books"] == book_borrowed:
                member["borrowed_books"].remove(book_borrowed)
                return {"message":"successfully returned"},200
            return{"message":"that wasnt the book boorrowed try again"},409
        return{"message":"wrong credentials"},400
    return {"message":"member not in our system"},404
def search_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name , id WHERE name = ?", (name,))
    row = cursor.rowcount
    if row is None:
        return {"message":"member not found"},404
    return {"name":row[0] , "id":row[1]},200
        


