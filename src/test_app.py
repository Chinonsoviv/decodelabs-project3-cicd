from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"DecodeLabs" in response.data
    print("Home route test passed")

def test_health_route():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    print("Health route test passed")

if __name__ == "__main__":
    test_home_route()
    test_health_route()
    print("All tests passed!")
