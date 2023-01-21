from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_all_problems():
    response = client.get("/records")
    assert response.status_code == 200
    assert response.json() == {"records": "all :^)"}


def test_problem():
    response = client.get("/records/1")
    assert response.status_code == 200
    assert response.json() == {"record_id": 1}
