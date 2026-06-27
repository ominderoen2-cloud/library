def validate_library_data(data , require_id = True):

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
        