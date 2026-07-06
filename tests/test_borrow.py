def test_successful_borrow(client):
    client.post("/member", json={
        "member_id": "M600",
        "name": "Roen"
    })

    client.post("/book", json={
        "book_id": "B600",
        "book_title": "Atomic Habits",
        "author": "James Clear",
        "availability": "available"
    })

    response = client.post("/borrow", json={
        "borrow_id": "BR600",
        "member_id": "M600",
        "book_id": "B600",
        "book_title": "Atomic Habits",
        "borrowed_at": "2026-06-29T10:00:00",
        "returned_at": None
    })

    assert response.status_code == 200
    assert response.json == {
        "message": "book successfully borrowed"
    }
def test_duplicate_borrow(client):
    client.post("/member", json={
        "member_id": "M600",
        "name": "Roen"
    })

    client.post("/book", json={
        "book_id": "B600",
        "book_title": "Atomic Habits",
        "author": "James Clear",
        "availability": "available"
    })

    payload = {
        "borrow_id": "BR600",
        "member_id": "M600",
        "book_id": "B600",
        "book_title": "Atomic Habits",
        "borrowed_at": "2026-06-29T10:00:00",
        "returned_at": None
    }

    # First borrow should succeed
    first = client.post("/borrow", json=payload)
    assert first.status_code == 200

    # Second borrow with the same borrow_id should fail
    response = client.post("/borrow", json=payload)

    assert response.status_code == 409
    assert response.json == {
        "message": "sorry borrow request unsuccessful"
    }
def test_return_book(client):
    client.post("/member", json={
        "member_id": "M700",
        "name": "Roen"
    })

    client.post("/book", json={
        "book_id": "B700",
        "book_title": "Clean Code",
        "author": "Robert Martin",
        "availability": "available"
    })

    client.post("/borrow", json={
        "borrow_id": "BR700",
        "member_id": "M700",
        "book_id": "B700",
        "book_title": "Clean Code",
        "borrowed_at": "2026-06-29T10:00:00",
        "returned_at": None
    })

    response = client.post(
        "/borrow/BR700/return",
        json={
            "book_id":"8700",
            "returned_at": "2026-06-30T10:00:00"
        }
    )

    assert response.status_code == 200
    assert response.json == {
        "message": "book successfully returned"
    }
def test_check_book_status(client):
    client.post("/book", json={
        "book_id": "B800",
        "book_title": "Python Crash Course",
        "author": "Eric Matthes",
        "availability": "available"
    })

    response = client.get("/borrow/B800")

    assert response.status_code == 200
    assert response.json == {
        "availability": "available"
    }
def test_check_book_status_after_borrow(client):
    client.post("/member", json={
        "member_id": "M801",
        "name": "Roen"
    })

    client.post("/book", json={
        "book_id": "B801",
        "book_title": "Fluent Python",
        "author": "Luciano Ramalho",
        "availability": "available"
    })

    client.post("/borrow", json={
        "borrow_id": "BR801",
        "member_id": "M801",
        "book_id": "B801",
        "book_title": "Fluent Python",
        "borrowed_at": "2026-06-29T10:00:00",
        "returned_at": None
    })

    response = client.get("/borrow/B801")

    assert response.status_code == 200
    assert response.json == {
        "availability": "borrowed"
    }
def test_return_nonexistent_borrow(client):
    response = client.post(
        "/borrow/BR999/return",
        json={
            "returned_at": "2026-06-30T10:00:00"
        }
    )

    assert response.status_code == 400
    assert response.json == {
        "message": "book  return unsuccessfull"
    }
def test_book_not_found_status(client):
    response = client.get("/borrow/B999")

    assert response.status_code == 404
    assert response.json == {
        "message": " book not found"
    }