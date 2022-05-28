"""
Test main.py modult
"""
import sys

from fastapi.testclient import TestClient
from main import app

sys.path.append("..")

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert list(response.json().keys()) == ['gregorian', 'hijri', 'coptic', 'quote']