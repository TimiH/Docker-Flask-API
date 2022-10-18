import json

#Given, When, Then framework for Test design
def test_ping(test_app):
    #Given
    client = test_app.test_client()
    #When
    response = client.get('/ping')
    data = json.loads(response.data.decode())
    #Then
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert data['message'] == 'pong!'
