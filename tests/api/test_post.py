def test_create_user(api_session):
    payload = {
        "name": "Lewis",
        "job": "driver"
    }
    response = api_session.post('https://reqres.in/api/users', json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Lewis"
    assert data["job"] == "driver"
    assert "id" in data
    assert "createdAt" in data