def test_create_member(client):
    response = client.post("/member" , json = {"id":"8" , "name":"roen"})
    assert response.status_code == 201
    assert response.get_json()["message"] == "member successfully registered"
def test_duplicate(client):
    payload = {"id":"9" , "name":"roy"}
    client.post(json=payload)
    response = client.post(json=payload)
    assert response.status_code == 409
    assert response.get_json()["message"] == "member already exists"
