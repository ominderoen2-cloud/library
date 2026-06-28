def validate_member_data(data , require_id = True):

    member_id = data.get("id")
    name = data.get("name")
    if require_id:
        if not member_id or name is None:
            return None , {"message":"missing credentials"} , 400
    if name is None :
        return  None , {"message":"missing credentials"} , 400
    return {
        "id":member_id , "name":name
    } , None , None
def validate_book_data(data , book_available = True):
    book_id = data.get("book_id")
    book_title = data.get("book_title")
    author = data.get("author")
    availability = data.get("availability")
    if  book_available:
        if not book_id or not book_title or  author is None:
         return None , {"message":"missing credentials"},400
    if not book_available:
        return {"message":"book is not availabble"},400
    return {
        "book_id":book_id , "book_title":book_title , "author":author , "availability":availability
    }, None , None
def validate_borrow_book_data(data , require_id = True):
    borrow_id = data.get("borrow_id")
    member_id = data.get("member_id")
    book_id = data.get("book_id")
    book_title = data.get("book_title")
    borrowed_at = data.get("borrowed_at")
    returned_at = data.get("returned_at")
    if require_id:
        if borrow_id is None :
            return None , {"message":"missing credentials"}, 400
        if not  member_id or not book_id or book_title is None:
            return None , {"message":"missing credentials"},400
    return {
        "borrow_id":borrow_id ,"member_id":member_id , "book_id":book_id , "book_title":book_title , "borrowed_at":borrowed_at , "returned_at":returned_at
    } , None , None


    #library/validators/validators.py

