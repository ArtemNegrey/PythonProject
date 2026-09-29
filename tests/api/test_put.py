def test_update_user(api_session):
    payload = {
        "name": "Cristiano",
        "job": "player"
    }
    response = api_session.put('https://reqres.in/api/users/2', json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["job"] == "player"
    assert "updatedAt" in data