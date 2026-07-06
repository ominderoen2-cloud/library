def test_create_book(client):
    response = client.post("/book", json={
        "book_id": "B001",
        "book_title": "Atomic Habits",
        "author": "James Clear",
        "availability": "available"
    })

    assert response.status_code == 201
    assert response.json == {
        "message": "book successfully registetred"
    }
def test_duplicate_book(client):
    payload = {
    "book_id": "B001",
    "book_title": "Atomic Habits",
    "author": "James Clear",
    "availability": "available"
                        }

    client.post("/book", json=payload)
    response = client.post("/book", json=payload)

    assert response.status_code == 409
def test_list_book(client):

    client.post("/book", json = {"book_id": "B001",
    "book_title": "Atomic Habits",
    "author": "James Clear",
    "availability": "available"})
    response = client.get("/book")

    assert response.status_code == 200
    assert["B001" , "Atomic Habits" , "James Clear" , "available"]
def test_get_one(client):
    client.post ("/book" , json = {"book_id":"B001" , "book_title":"Atomic Habits" , "author":"James Clear" , "availability":"available"})
    response = client.get("/book/B001")
    assert response.status_code == 200
    assert response.json == {"book_id":"B001" , "book_title":"Atomic Habits" , "author":"James Clear" , "availability":"available"}
def test_book_not_found(client):

    response = client.get("/book/DOESNTEXIST")
    assert response.status_code == 404
    assert response.json == {"message":"book not available"}
def test_delete_book(client):
    client.post("/book", json={
        "book_id": "B001",
        "book_title": "Atomic Habits",
        "author": "James Clear",
        "availability": "available"
    })
    response = client.delete("/book/B001")
    assert response.status_code == 200
    assert response.json == {"message":"book successfuly deleted"}