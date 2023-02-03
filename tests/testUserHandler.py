from fastapi.testclient import TestClient
from main import app
import os

os.environ["TEST"] = "1"

client = TestClient(app)


def test_user_get_handler():
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Martin"}


def test_user_post_handler():
    response = client.post("/user", json={"name": "Martin"})
    assert response.status_code == 200


def test_user_get_all_handler():
    response = client.get("/user")
    assert response.status_code == 200
    assert len(response.json().keys()) == 1
    assert response.json()["1"] == {"id": 1, "name": "Martin"}
