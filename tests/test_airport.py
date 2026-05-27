from urllib import response

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_airports_default_pagination():
    response = client.get("/aeroporti")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert isinstance(data["data"], list)
    assert len(data["data"]) >= 1

def test_get_airports_with_pagination():
    response = client.get("/aeroporti?pages=1&size=1")
    assert response.status_code == 200

    data = response.json()
    assert len(data["data"]) == 1

def test_get_airport_not_found():
    response = client.get("/aeroporti/999")
    assert response.status_code == 404

def test_get_airport_success():
    response = client.get("/aeroporti/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1