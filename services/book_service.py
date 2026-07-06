from database.database import book_returned , book_borrowed , add_book , add_borrow_record, add_return_record , get_book_status , list_books , delete_book , connect_db
from validators.validators import validate_book_data , validate_borrow_book_data , validate_return_book_data
class BookService:
    def create_book(self ,data):
         clean_data , error , status = validate_book_data(data)
         if error :
            return error , status
         success = add_book(clean_data["book_id"] , clean_data["book_title"] , clean_data["author"] , clean_data["availability"])
         if not success:
              return{"message":"book not registered"}, 409
         return {"message":"book successfully registetred"},201

    def get_all_books(self):
        return list_books(),200
    def get_one_book(self , book_id):
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
    def check_book_status(self , book_id):
        status = get_book_status(book_id)
        if status is None:
           return{"message":" book not found"}, 404
        if status[0] == "available":
           return {"availability":"available"}, 200
        return {"availability":"borrowed"}, 200
    def remove_book(self , book_id):
        success = delete_book(book_id)
        if not success:
           return {"message":"book not found"}, 404
        return {"message":"book successfuly deleted"}, 200