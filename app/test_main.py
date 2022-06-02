from fastapi.testclient import TestClient
import pytest
from .main import app

client = TestClient(app)


def test_exceptions():
    response = client.post("/search", json={"text": "XXX"})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "the payload don't start with a index like 'A', 'B', 'E' etc. it start with a roman number"
    }


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"text": "AXXBLX"}, {"number": "LX", "value": 60}),
        ({"text": "AXXXBLXX"}, {"number": "LXX", "value": 70}),
        # mutiples index test
        ({"text": "AXXXBLXXEMFCC"}, {"number": "M", "value": 1000}),
        # test with values like IV, IX, XL etc
        ({"text": "AXXIXBCCXCIV"}, {"number": "CCXCIV", "value": 294}),
    ],
)
def test_read_main(test_input, expected):
    response = client.post("/search", json=test_input)
    assert response.status_code == 200
    assert response.json() == expected
