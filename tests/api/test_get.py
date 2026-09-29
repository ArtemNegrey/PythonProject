def test_get_user(api_session):
    response = api_session.get('https://reqres.in/api/users/2')

    assert response.status_code == 200

    data = response.json()
    assert data["data"]["id"] == 2
    assert data["data"]["first_name"] == "Janet"