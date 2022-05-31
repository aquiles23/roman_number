from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/search", json={"text": "AXXBLX"})
    assert response.status_code == 200
    assert response.json() == {"number": "LX", "value": 60}
