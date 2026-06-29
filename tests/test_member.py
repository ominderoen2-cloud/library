def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json == {"status": "api running"}
def test_create_member(client):
    response = client.post("/member" , json = {"id":"M103" , "name":"roen"})
    assert response.status_code == 201
    assert response.json == {"message":"member successfully registered"}
def test_duplicate_member(client):
    payload ={"id":"M1o3" , "name":"jim"}
    client.post("/member" ,  json = payload)
    response = client.post("/member" , json = payload)
    assert response.status_code == 409
    assert response.json == {"message":"member not registered"}
def test_list_member(client):
    client.post("/member" , json = {"id":"M290" , "name":"ALICE"})
    response = client.get("/member")
    assert response.status_code == 200
    assert ["M290" , "ALICE"] in response.json
def test_get_member(client):
    client.post("/member", json={
        "id": "M300",
        "name": "Bob"
    })

    response = client.get("/member/M300")

    assert response.status_code == 200
    assert response.json == {"member_id":"M300", "name":"Bob"}
def test_member_not_found(client):
    response = client.get("/member/DOESNOTEXIST")

    assert response.status_code == 404
    assert response.json == {
        "message": "member not found"
    }
def test_update_member(client):
    client.post("/member", json={
        "id": "M400",
        "name": "John"
    })

    response = client.put(
        "/member/M400",
        json={
            "name": "Johnny"
        }
    )

    assert response.status_code == 200
    assert response.json == {
        "message": "member successfully updated"
    }
def test_delete_member(client):
    client.post("/member", json={
        "id": "M500",
        "name": "Mike"
    })

    response = client.delete("/member/M500")

    assert response.status_code == 200
    assert response.json == {
        "message": "successfully deleted"
    }