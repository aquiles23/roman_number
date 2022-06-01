from fastapi.testclient import TestClient
import pytest
from .main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"text": "AXXBLX"}, {"number": "LX", "value": 60}),
        ({"text": "AXXXBLXX"}, {"number": "LXX", "value": 70}),
        (None, 'Welcome')
    ],
)
def test_read_main(test_input, expected):
    response = client.get("/search", json=test_input)
    assert response.status_code == 200
    assert response.json() == expected
