import requests

def test_requests():
    response = requests.get('https://api.github.com')
    assert response.status_code == 200
