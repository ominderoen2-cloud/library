from database.database import book_returned , add_return_record
from validators.validators import validate_return_book_data
class Returnbookservice:
     def return_book(self ,data , borrow_id ):
        clean_data , error , status = validate_return_book_data(data)
        if error :
           return error , status
        success = add_return_record( clean_data["returned_at"] , borrow_id )
        if not success:
        
           return {"message":"book  return unsuccessfull"}, 400
        book_returned( clean_data["book_id"])
        return {"message":"book successfully returned"}, 200