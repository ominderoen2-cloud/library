from database.database import add_borrow_record , book_borrowed
from validators.validators import validate_borrow_book_data
class Borrowbookservice:
    def borrow_book(self , data):
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
    

    
    
