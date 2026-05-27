from urllib import response

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_airports_default_pagination():
    response = client.get("/aeroporti")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1