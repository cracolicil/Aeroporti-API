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

def test_create_airport():
    body = {
        "codice": "SLT",
        "citta": "Salsomaggiore Terme"
    }
    response = client.post("/aeroporti", json=body)
    assert response.status_code == 201
    data = response.json()
    assert data["codice"] == body["codice"]
    assert "id" in data

def test_create_airport_fail():
    body = {
        "codice": "FD",
        "citta": "Fidenza"
    }
    response = client.post("/aeroporti", json=body)
    assert response.status_code == 422

def test_delete_airport_success():
    response = client.delete("/aeroporti/1")
    assert response.status_code == 204

def test_delete_airport_fail():
    response = client.delete("/aeroporti/999")
    assert response.status_code == 404