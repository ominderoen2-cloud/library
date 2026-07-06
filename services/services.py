from validators.validators import validate_member_data , validate_book_data , validate_borrow_book_data, validate_return_book_data
from database.database import add_member , get_all_members , update_member_data , delete_member, connect_db , add_book , list_books, delete_book, add_borrow_record , add_return_record , book_borrowed , book_returned, get_book_status

def create_member(data):
    clean_data , error , status = validate_member_data(data)
    if error:
        return error , status
    success = add_member(clean_data["member_id"] , clean_data["name"])
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
    clean_data , error , status = validate_member_data(data , require_id=False)
    if  error:
     return error , status
    success = update_member_data(clean_data["name"] , member_id)
    if not success:
        return {"message":"member not updated"},400
    return {"message":"member successfully updated"} , 200
def get_by_member_id(member_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT member_id , name FROM members WHERE member_id = %s" , (member_id,))
    row = cursor.fetchone()
    if row is None :
        return {"message":"member not found"} , 404
    conn.close()
    return {
    "member_id": row[0],
    "name": row[1]
}, 200
def create_book(data):
    clean_data , error , status = validate_book_data(data)
    if error :
        return error , status
    success = add_book(clean_data["book_id"] , clean_data["book_title"] , clean_data["author"] , clean_data["availability"])
    if not success:
        return{"message":"book not registered"}, 409
    return {"message":"book successfully registetred"},201

def get_all_books():
    return list_books(),200
def get_one_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT book_id , book_title , author , availability FROM books WHERE book_id = %s", (book_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return{"message":"book not available"}, 404
    return {
    "book_id": row[0],
    "book_title": row[1],
    "author": row[2],
    "availability": row[3]
}, 200
def borrow_book(data):
        clean_data , error , status = validate_borrow_book_data(data)
        if error :
            return error , status
        success = add_borrow_record( clean_data["borrow_id"],
                                     clean_data["member_id"] 
                                    , clean_data["book_id"],
                                    clean_data["book_title"],
                                    clean_data["borrowed_at"],
                                    None,
                                    )
        if success :
            book_borrowed(clean_data["book_id"])
            return {"message":"book successfully borrowed"},200
        return {"message":"sorry borrow request unsuccessful"},409

def return_book(data , borrow_id ):
    clean_data , error , status = validate_return_book_data(data)
    if error :
        return error , status
    success = add_return_record(clean_data["returned_at"] , borrow_id )
    if not success:
        
        return {"message":"book  return unsuccessfull"}, 400
    book_returned(clean_data["book_id"])
    return {"message":"book successfully returned"}, 200
def remove_book(book_id):
    success = delete_book(book_id)
    if not success:
        return {"message":"book not found"}, 404
    return {"message":"book successfuly deleted"}, 200
def check_book_status(book_id):
    status = get_book_status(book_id)
    if status is None:
        return{"message":" book not found"}, 404
    if status[0] == "available":
        return {"availability":"available"}, 200
    return {"availability":"borrowed"}, 200
#library/services/services.py
        


